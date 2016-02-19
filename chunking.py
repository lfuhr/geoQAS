'''
Does basic gammar analysis.
'''
import nltk, questions, stanford
import doctest # Tests aufrufen mit >>> python3 -m doctest -v chunking.py
import answertypes; from answertypes import *
import predicates; from predicates import *
import precise; from precise import *
from nltk import Tree


# Example Tree in nltk
#Tree("S", [("The","DT"),Tree("PROPERTY", [("address","NN"), ("of","INO")]), Tree("INSTANCE", [("Padu","NNP")]), ("?",".")])

# INO is the preposition of

class Question:
    'This class Contains a Question and does most of the question analysis'
   

    _grammar = """
        PROPERTY: {<MD><PRP><VB>}
        RETURN_PROPERTY: {<NNS?><INO>}
        INSTANCE: {<DT>?(<NNP>|<PRP>)<CD>?(<INO>?<NNP>)?}
        CLASS: {<DT>?<RB>*<JJ>*<NNS?>+}        
        PROPERTY: {<VB.*>?<EX>?(<RB>|<IN>)*}
        PROPERTY: {<DT><JJ.*>}
        PROPERTY: {<TO>}
        VALUE: {<CD>}
    """

    # Generate those Objects just once
    _regexparser = nltk.RegexpParser(_grammar)
    _lemmatizer = nltk.stem.WordNetLemmatizer()

    _stan_tag = lambda x : stanford.pos_tagger.tag(nltk.word_tokenize(x))

    def _of_as_tag(tagged_sent):
        """ Assigns of to its own tag 
        >>> print(Question._of_as_tag([("of","IN")]))
        [('of', 'INO')]
        """
        i = 0
        for e in tagged_sent:
            if e[0] == "of": tagged_sent[i] = ("of", "INO")
            i += 1
        return tagged_sent
    


    def _untag_chunk(chunk):
        """Returns lowercase string without articles 
        >>> print(Question._untag_chunk(Tree("OBJ", [("The","DT"), ("brown","VB"), ("Fox","NN")])))
        brown fox
        """
        return " ".join(
            [tuple_[0].lower() for tuple_ in chunk if tuple_[1] != 'DT']
        )
   



    def __init__(self, sentence):
        """ Does all the work """
        self.sentence = sentence
        self.tagged   = Question._stan_tag(sentence)
        self.tagged   = Question._of_as_tag(self.tagged)
        question_word, self._answertype, q_without_qword = answertypes.calc_answertype(self.tagged)
        # Debuging info
        # print(str(question_word) +str(self._answertype) + str(q_without_qword))
        self.chunked  = Question._regexparser.parse(q_without_qword)

        rm_lst = []
        for chunk in self.chunked:
            if type(chunk) is not nltk.tree.Tree: rm_lst.append(chunk)
        for chunk in rm_lst : self.chunked.remove(chunk)

        # Iterate over everything
        i=0
        for chunk in self.chunked:
            j = 0
            for tup in chunk:
                if tup[1] == "DT" : chunk.remove(tup) #Remove determiners
                else:
                    if tup[1] == "NNS":
                        chunk[j] = (Question._lemmatizer.lemmatize(tup[0]), "NNS") #singular
                    j += 1
            
            # Extract descriptive prefixes of classes
            if chunk.label() == "CLASS" and chunk[0][1].startswith("JJ"):
                self.chunked.insert(i,Tree("DESCRIPTIVE", [chunk[0]]))
                chunk.remove(chunk[0])
            
            # Range is a property
            elif chunk.label() == "RETURN_PROPERTY" and chunk[0][0] == "range":
                chunk.set_label("PROPERTY")

            i+=1




    def get_answertype(self):
        """Return the answer type of a question
        >>> print(Question("How many restaurants are in Passau?").get_answertype())
        count
        """
        return self._answertype

    def get_tree(self) :
        return self.chunked
