"""
Converts a precise question object to a SPARQL Query.
"""
import classifier
import wn_dictionary
import property_lexicon
import chunking
import calcDuration
import math

_ANSWER_VAR = " ?a "
_ADDRESS_VARS = " ?street ?number ?city "
_POSITION_VARS = " ?lat ?long "
_NAME_VAR = " ?name "
_STREET_VAR = " ?street "
_NUMBER_VAR = " ?number "
_CITY_VAR = " ?city "
_LATITUDE_VAR = " ?lat "
_LONGITUDE_VAR = " ?long "
_FROM = "?from"
_TO = "?to"


DISTANCE = " bif:st_distance (?geo_a, ?geo_b) as ?distance "


vars_mapping = {
                    #"address" : _STREET_VAR + " " + _NUMBER_VAR + " " + _CITY_VAR, # city is often not available
                    "address" : _NAME_VAR + " " + _STREET_VAR + " " + _NUMBER_VAR,
                    "name" : _ANSWER_VAR,
                    "location" : _NAME_VAR + " " + _STREET_VAR + " " + _NUMBER_VAR + " " + _LATITUDE_VAR + " " + _LONGITUDE_VAR,
                }

# Creates triples out of the (subject, property, object) tree #
def create_triples(triples, filters, var, answer_type, tuple_, groupby="", having="", orderby="", limit=0) :

    # variable 'var': 1st iteration: ''+'a' = 'a', 2nd 'aa' and 'ab', ... -> no conflicts with variables in the query
    rec_var = 'a' # variable which is appended to current variable 'var', e.g. 'b'+'a'='ba' for 1st object, 'b'+'b'='bb' for 2nd object, ...

    subject = tuple_[0] # subject is first component of the tuple
    properties = tuple_[1] # (property, object) tuples are the second component as a list

    # append triples for rdf:type or rdfs:label
    if (isAddress(subject[0])) :
        address_ = subject[0].split()
        triples += address(var, "'" + address_[0] + "'", "'" + address_[1] + "'")
    elif (subject[1] == "CLASS") :
        triples += type_(var, get_class_name(subject[0]))
    elif (subject[1] == "INSTANCE") :
        triples += name(var, "'" + subject[0] + "'")
    else :
        raise RuntimeError("Illegal subject type: " + subject[1] + " in subject " + str(subject))

    # properties = [('located in', (('Passau', 'INSTANCE'), []))])
    for (property_, object_) in properties :
    
        # add triples for objects recursively
        if (isinstance(object_, tuple) and property_ != "type" and property_ != "located in" and not property_.startswith("range")) : # 'located in' and 'range' recursion is handled externally because of UNION operator
            temp = create_triples(triples, filters, var+rec_var, answer_type, object_, groupby, having, orderby, limit)
            triples = temp[0]
            filters = temp[1]
            groupby = temp[2]
            having = temp[3]
            limit = temp[6]
    
        if (property_ == "type") :
            class_ = classifier.synonym(subject[0])
            type_property = property_lexicon.properties_by_type.get(class_, "")
            
            # In case that there is no type information use class without its type, e.g. 'touristic castle' -> 'castle'
            if (type_property == "") :
                print("\nNo type information available for class '" + class_ + "'!")
            else :
                if (isinstance(object_, str)) :
                    triples += "?" + var + " " + type_property + " '" + str(object_).lower() + "' . "
                else :
                    triples += "?" + var + " " + type_property + " " + _NAME_VAR + " . "
                    answer_type = "type" # answer type is changed due to conflicts with name for results -> value
                    
        elif (property_ == "typeof") :
            type_property = property_lexicon.properties_by_type[subject[0]]
            triples += "?" + var+rec_var + " " + type_property + " ?" + var + " . "
            
        elif (property_ == "address") :
            triples += address(var)
            
        elif (property_ == "located in" or property_.startswith("range")) :
        
            range_ = 5
            if (property_.startswith("range")) :
                range_ = float(property_.split(":")[1])
        
            var_sub = var
            var_obj = var+rec_var
            #triples += geometries(var_sub, var_obj)
            #filters += " AND " + filter_in_range(range_, var_sub, var_obj) + " "
            
            temp = create_triples("", "", var+rec_var, answer_type, object_, groupby, having, orderby, limit)
            triplesInside = temp[0]
            filtersInside = temp[1]
            
            triples += " { {" + geometries(var_sub, var_obj) + triplesInside + " FILTER(" + filter_in_range(range_, var_sub, var_obj) + ") } UNION "
            triples += "{ ?" + var_sub + " <http://linkedgeodata.org/ontology/addr%3Astreet> '" + object_[0][0] + "' . } } . "
            
        elif (property_ == "closest to") :
            triples += geometries(var, var+rec_var)
            filters += " AND (bif:GeometryType (?geo_" + var + ") = 'POINT') "
            limit = 1
            triples += " BIND(" + distance(var, var+rec_var) + " as ?distance) . "
            
        elif (property_ == "distance") :
            triples += geometries_(var, var+rec_var, _FROM, _TO)
            triples += " BIND( bif:st_distance (" + _FROM + ", " + _TO + ") as ?distance) . "
            filters += " AND (bif:GeometryType (" + _FROM + ") = 'POINT') AND (bif:GeometryType (" + _TO + ") = 'POINT')"
        
        elif (property_.startswith("duration")) :
            mode = property_.split(":")[1]
            triples += geometries_(var, var+rec_var, _FROM, _TO)
            triples += " BIND( bif:st_distance (" + _FROM + ", " + _TO + ") * " + calcDuration.minutes_it_takes_string(mode) + " as ?duration) . "
            filters += " AND (bif:GeometryType (" + _FROM + ") = 'POINT') AND (bif:GeometryType (" + _TO + ") = 'POINT')"
            
        else :
            raise RuntimeError("Unmatched property while building SPARQL query: " + property_)
    
        # get the next variable name which has not been used before
        rec_var = fresh(rec_var)

    return (triples, filters, groupby, having, var, orderby, limit)

# Builds the SPARQL query for an analyed question #
def create_query(question) :
    answer_type = question.answertype
    attr = question.attribute
    tuple_ = (question.subject, question.properties)
    var = 'a'
    triples = ""
    filters = ""
    groupby = ""
    #print(tuple_)

    # Triples have to be added in order to return the searched property or name instead of the IRI
    if (attr == "location") :
        triples += coordinates(_ANSWER_VAR, _LATITUDE_VAR, _LONGITUDE_VAR)
        triples += name(var, _NAME_VAR)
        triples += " OPTIONAL {" + address(var) + "} "
    elif (attr == "address") :
        triples += address(var)
        triples += name(var, _NAME_VAR)
    elif (attr == "name") :
        next_ = fresh(var)
        triples +=  name(next_, "?" + var)
        groupby += "?" + next_
        filters += 'AND (lang(?' + var + ') = "" )' # Use the locations local language for names -> many places do not have language specific names (e.g. Passau in English)
        var = next_
    elif (attr == "type") :
        next_ = fresh(var)
        type_property = property_lexicon.properties_by_type[question.subject[0]]
        triples += "?" + next_ + " " + type_property + " ?" + var + " . "
        var = next_
    elif (attr != "") :
        next_ = fresh(var)
        triples += "?" + next_ + " " + attr + " ?" + var + " . "
        var = next_
    
    result = create_triples(triples, filters, var, answer_type, tuple_, groupby)
    return format_query(result, answer_type, attr)

    

### Help methods for dynamical combination of relationships to build the query ###

# Name relationship
def name(var, name) :
    return "?" + var + " rdfs:label " + name + " . "

# Type relationship
def type_(x, t) :
    return "?" + x + " rdf:type " + t + " . "

# Address, no '?' needed for variable names
def address(x, street="?street", number="?number") :
    return " ?" + x + " <http://linkedgeodata.org/ontology/addr%3Astreet> " + street + " . ?" + x + " <http://linkedgeodata.org/ontology/addr%3Ahousenumber> " + number + " . " # city is often not available
    # return " ?" + x + " <http://linkedgeodata.org/ontology/addr%3Astreet> ?street . ?" + x + " <http://linkedgeodata.org/ontology/addr%3Ahousenumber> ?number . ?" + x + " <http://linkedgeodata.org/ontology/addr%3Acity> ?city . "

# Longitude and latitude
def coordinates(x, latitude, longitude) :
    return x + " lgdgeo:long " + longitude + " ; lgdgeo:lat " + latitude + " . "

# see constant DISTANCE
def distance(x, y) :
    return " bif:st_distance (?geo_" + x + ", ?geo_" + y + ") "

# Geometry for an object for distance and range filter
def geometry(x) :
    return " ?" + x + " geom:geometry  [ geo:asWKT ?geo_" + x + " ] . "

# Geometries for two objects for distance and range filter
def geometries(x, y) :
    return " ?" + x + " geom:geometry  [ geo:asWKT ?geo_" + x + " ] . ?" + y + " geom:geometry  [ geo:asWKT ?geo_" + y + "] . "
    
def geometries_(x, y, geo_x, geo_y) :
    return " ?" + x + " geom:geometry  [ geo:asWKT " + geo_x + " ] . ?" + y + " geom:geometry  [ geo:asWKT " + geo_y + "] . "

# Range filter for x and y in range 'range_'
def filter_in_range(range_, x, y) :

    if (range_ < 0) :
        raise RuntimeError("Range request has a negative range: " + range_)

    # range has to be followed by its exponent, i.e. 5 -> 5.1, 12 -> 12.2, 100 -> 100.3
    range_ = math.ceil(range_)
    exp = math.floor(math.log10(range_)) + 1
    r = str(range_) + "." + str(exp)

    return "bif:st_within (?geo_" + x + ", ?geo_" + y + ", " + r + ")"

### Returns the next variable, i.e. 'b' for 'a'. ###
def fresh(var) :
    return chr(ord(var)+1)

# Returns the full class IRI for a name #
def get_class_name(name) :
    class_name = wn_dictionary.wn_lexicon.get(name.title(), "")
    if (len(class_name) == 0) :
        class_name = classifier.classify(name.title())
    return classifier.classify(name.title())

## Returns if the provided string is an address, e.g. 'Innstraße 33' -> true, 'restaurant' -> false
def isAddress(string) :
    words = string.split()
    
    # Address consists of street and number only
    if (len(words) != 2) : return False
    
    number = 0
    try :
        return int(words[1]) != 0
    except ValueError :
        return False

### Builds a query out of its components, i.e. triples, filters, groupby, having, orderby and limit. ###
def format_query(tuple_, answertype, attribute) :

    # tuple = (triples, filters, groupby, having, var, orderby, limit)
    triples = tuple_[0]
    filters = tuple_[1]
    groupby = tuple_[2]
    having = tuple_[3]
    orderby = tuple_[5]
    limit = tuple_[6]
    
    # create select/ask statement
    # answertype = exists, count, value, distance
    query = ""
    if (answertype == "exists") :
        query += "ASK "
    elif (answertype == "count") :
        query += "SELECT COUNT (DISTINCT " + vars_mapping.get(attribute, _ANSWER_VAR) + ")"
    elif (answertype == "value") :
        vars_ = vars_mapping.get(attribute, _ANSWER_VAR)
        query += "SELECT DISTINCT " + vars_
        orderby += _NAME_VAR  if _NAME_VAR in vars_ else _ANSWER_VAR if (_ANSWER_VAR in vars_) else ""
    elif (answertype == "distance") :
        query += "SELECT ?distance"
        orderby += " ?distance "
    elif (answertype == "duration") :
        query += "SELECT ?duration"
        orderby += " ?duration "
    else :
        raise RuntimeError("Answer type '" + answertype + "' is not supported in query_creator.format_query()!")

    # Queries except 'ASK' need 'WHERE'
    if (answertype != "exists") :
        query += " WHERE "

    # Modifications for subquery in order to apply the MIN function
    if (limit == 1) :
        query += "{" # follows 'WHERE'
        query += " { SELECT" + vars_mapping.get(attribute, _ANSWER_VAR) + " ?distance WHERE " # only distance supported for minima so far

    # add triples
    query += " { " + triples
    
    # add filters if necessary
    if (len(filters) > 0) :
        query += "FILTER(" + filters[4:] + ")" # AND has to be removed
    query += " } "
    
    # group by
    if (len(groupby) > 0) :
        query += " GROUP BY " + groupby + " "
    
    # Modifications for subquery in order to apply the MIN function
    if (limit == 1) :
        query += " ORDER BY ?distance } }" # end sub query
    
    # having
    if (len(having) > 0) :
        query += " HAVING " + having

    # order by
    if (len(orderby) > 0 and not limit > 0) :
        query += " ORDER BY " + orderby
    
    # limit
    if (limit > 0) :
        query += " LIMIT " + str(limit)
    
    return query


