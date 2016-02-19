"""
Handles the projection between words and classes in the dataset.
"""
import database
import query_creator
import wn_dictionary
from nltk.corpus import wordnet as wn

# Returns the class IRI for a name string like "Restaurant" or "" if no match has been found.
def get_class_name(entity_name) :

    # street is mapped wrong -> extra case here
    if (entity_name.lower() == "street") :
        return "http://linkedgeodata.org/ontology/ResidentialHighway"
        
    class_name = wn_dictionary.wn_lexicon.get(entity_name.title(), "")
    return class_name[1:-1]

# Returns a classified synonym for a noun which is in the dataset.
def synonym(noun) :
    syns = synonyms(noun)
    keys = wn_dictionary.wn_lexicon.keys()
    name = ""
    for syn in syns :
        if (syn in keys) :
            name = syn
            break;
    
    if (name == "") :
        raise RuntimeError("No class found for '" + noun + "'")
    
    return name.lower()
        

# Returns all synonyms for a word in natural language using wordnet.
def synonyms(word) :
    """Returns lowercase string without articles 
    >>> print(synonym("eatery"))
    restaurant
    """
    synsets = wn.synsets(word)    
    syns = set()
    for synset in synsets : # different meanings of a word e.g. 'bank'
        for syn in synset.lemma_names() : # names for each different meaning
            syns.add(syn.title()) # add all synonym names to the result set
    
    return syns

# Classifies a name string like "Restaurants", i.e. it uses word net and returns the class IRI for the entity.
def classify(entity_name) :

    class_name = get_class_name(entity_name)
    
    # If there is no class for the name, use wordnet and look for classes synonyms
    if (len(class_name) == 0) :
        # use wordnet and try again
        wn_words = synonyms(entity_name)
        for word in wn_words :
             class_name = get_class_name(word)
             # first match is used
             if (len(class_name) > 0) :
                break
    
    # If the string has several tokens like 'ice cream shop' try again with parts 'ice cream' and 'cream shop'
    words = entity_name.split()
    if (len(class_name) == 0 and len(words) > 1) :
        try :
            class_name = classify(' '.join(words[:-1]))[1:-1] # <> have to be removed
        except RuntimeError :
            class_name = ""
        
        if (class_name == "") :
            try :
                class_name = classify(' '.join(words[1:]))[1:-1] # <> have to be removed
            except RuntimeError :
                class_name = ""
    
      
    # In case that wordnet could not discover any classes throw error
    if (len(class_name) == 0) :
        raise RuntimeError("No class found for '" + entity_name + "'")
    
    return "<" + class_name + ">"
