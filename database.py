"""
Passes the complete query to the database specified in the config file
"""
import urllib.request
import urllib.parse
import json
import conf

#server = conf.endpoint + "Query"
server = "http://lod.openlinksw.com/sparql/"
#server = "http://linkedgeodata.org/sparql/"
#server = "http://geo.linkeddata.es/sparql/"
#args = "?view=HTML&handle=download"
args = "?default-graph-uri="
query_arg_name = "&query="
#format_arg = "&format=SPARQL%2FJSON#1062461258"
format_arg = "&should-sponge=&format=application%2Fsparql-results%2Bjson&CXML_redir_for_subjs=121&CXML_redir_for_hrefs=&timeout=30000&debug=on"

_prefixes = """PREFIX lgd:<http://linkedgeodata.org/triplify/>
PREFIX lgdgeo:<http://www.w3.org/2003/01/geo/wgs84_pos#>
PREFIX lgdont:<http://linkedgeodata.org/ontology/>
PREFIX geonames:<http://www.geonames.org/ontology#>
PREFIX clc: <http://geo.linkedopendata.gr/corine/ontology#>
PREFIX gag: <http://geo.linkedopendata.gr/greekadministrativeregion/ontology#>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
PREFIX geor: <http://www.opengis.net/def/rule/geosparql/>
PREFIX strdf: <http://strdf.di.uoa.gr/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX uom: <http://www.opengis.net/def/uom/OGC/1.0/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX geom: <http://geovocab.org/geometry#>
"""

def create_url(query) :
    formatted_query = urllib.parse.quote(_prefixes + query)
    return server + args + query_arg_name + formatted_query + format_arg

def execute(query) :
    url = create_url(query)
    response = ""
    try :
        response = urllib.request.urlopen(url)
        str_response = response.read().decode('utf-8')
        data = json.loads(str_response)
        response.close()
    except urllib.error.HTTPError as error:
        print('Error on communication with server: Code ' + str(error.code) + ': ' + error.reason + '\n')
        data = {'head': {}, 'results': {'bindings': []}} # Dummy data, is interpreted as no result
    return data
