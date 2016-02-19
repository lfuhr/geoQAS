"""
Java specific things for integration of the StanfordPOSTagger
"""
import nltk
import nltk.tag.stanford
import os
from nltk.tag.stanford import StanfordPOSTagger
from nltk.tag import StanfordNERTagger

os.environ['CLASSPATH'] = 'stanford-postagger:stanford-ner'
os.environ['STANFORD_MODELS']='stanford-postagger/models:stanford-ner/classifiers'

pos_tagger = StanfordPOSTagger('english-bidirectional-distsim.tagger')
#ner_tagger = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz') 

if __name__ == "__main__":
    print(pos_tagger.tag('How many restaurants are in Passau?'.split()))
