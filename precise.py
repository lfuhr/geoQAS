'''
This Module receives a chunked question and does clarification and formalization
'''
import nltk, questions, stanford, doctest 
import answertypes; from answertypes import *
import predicates; from predicates import *
from nltk import Tree
import conf

class Precise :
    
    _join = lambda tree : " ".join([x[0] for x in tree.leaves()])
    _join_nominative = lambda tree : "  ".join([x[0] for x in tree.leaves() if x[1].startswith("NN")])

    def _process_verbal_query(self, index):
        import wiki_match
        searchKey = Precise._join(self.tree[index]) + " " + Precise._join(self.tree[index+1])
        self._noun_phrases.append((wiki_match.query(searchKey), "CLASS"))

    def _append_property(self, chunk):
        position = 0 if len(self._noun_phrases) < 2 else len(self._noun_phrases) - 1
        while len(self._predicatewords) <= position : self._predicatewords.append(Tree('Propertywords', []))
        self._predicatewords[position].append(chunk)
 
    def __init__(self, question):

        # Attributes of Precise object
        self.answertype = "count"
        self.attribute  = "name"
        self.subject    = ""
        self.properties = [] # predicate 
        self._noun_phrases = []
        self._predicatewords = []


        answertype = question.get_answertype()
        self.tree = question.get_tree()
        EMPTY_OBJECT = (("", "NONE"), [])
        looking_for_closest = False
        range_ = 0

        # Parse Sentence
        skip_one_in_for_loop = False
        for index, chunk in enumerate(self.tree):
            if skip_one_in_for_loop and chunk.label() != "DESCRIPTIVE":
                skip_one_in_for_loop = False
            elif chunk.label() == "PROPERTY":
                if index == 0 and chunk[0][1].startswith("VB"): # verb at beginning "eat food"
                    self._process_verbal_query(index)
                    skip_one_in_for_loop = True
                else:
                    self._append_property(chunk)

            elif chunk.label() in {"INSTANCE", "CLASS"} :
                joined = Precise._join(chunk)
                if joined == "distance" :
                    answertype = "distance"
                else:
                    resulttup = (joined, chunk.label())
                    if joined in {"home", "me"}:
                        resulttup = (conf.HOME, "INSTANCE") # to find home
                    self._noun_phrases.append(resulttup)

            elif chunk.label() == "DESCRIPTIVE":
                desc = Precise._join(chunk)
                self.properties.append(("type",desc))
            
            elif chunk.label() == "RETURN_PROPERTY" :
                self.attribute = Precise._join_nominative(chunk)

            elif chunk.label() == "VALUE":
                skip_one_in_for_loop = True
                value = Precise._join(chunk)
                metric = Precise._join(self.tree[index+1])
                if metric in {"km", "kilometer", "kilometre"}: pass
                elif metric in {"m", "meter", "metre"}: value = float(value) / 1000
                elif metric in {"mile", "mi"}: value = 1.8553 * float(value)
                else: raise Exception("unknown metric")
                range_ = value

        # Question word where -> give me location
        if answertype == "location" :
            self.answertype = "value"
            self.attribute = "location"
        else : self.answertype = answertype
        
        # That it counts items and not names
        if self.answertype != "value" and self.attribute == "name" :
            self.attribute = ""
        
        # Join the property words to a string (produces "predicate" variable)
        if self._predicatewords: predstring = Precise._join(self._predicatewords[0])
        else: predstring = ""
        predicate = predicates.convert(predstring)


        #if predicate and self.answertype in {"distance", "duration"}: print(predicate)
        if not predicate: # maybe predicate can be specified by answertype
            if self.answertype == "distance":
                predicate = "distance"
            elif self.answertype == "duration":
                if any(w in question.sentence for w in {"car", "drive"}):
                    predicate = "duration:car"
                else: predicate = "duration:pedestrian"
            
                        
        # Define near
        if predicate == "near" : predicate = "range:"+str(conf.NEAR)
        elif predicate == "range": predicate = "range:"+str(range_)
 
        # Append property with object to array
        if predicate != "":
            if self._noun_phrases[1:] :
                self.properties.append((predicate, (self._noun_phrases[1],[])))
            elif predicate in {"closest to", "distance"} or predicate.startswith("duration"):
                self.properties.append((predicate,((conf.HOME,"INSTANCE"),[])))

        if len(self._predicatewords) > 1: # more properties and nps
            predstring = Precise._join(self._predicatewords[0])
            predicate = predicates.convert(predstring)
            if predicate == "near" : predicate = "range:"+str(conf.NEAR)
            elif predicate == "range": predicate = "range:"+str(range_)
            if predicate: self.properties.append((predicate, (self._noun_phrases[2],[])))

        self.subject = self._noun_phrases[0]
