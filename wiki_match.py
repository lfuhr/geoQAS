"""
Implementation of the dictionary lookup approach (common knowledge)
"""
from __future__ import division
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from functools import reduce
import os

STEMMED_PAGES = 'common_knowledge/wiki_pages/stemmed_user'

def fileNames(root) :
    names = []
    for root, dirs, files in os.walk(root) :
        for file_ in files :
            names.append(root + '/' + file_)
    return names

def read(f_path) :
    f = open(f_path, 'r', encoding='utf8', errors='replace')
    text = f.read()
    f.close()
    return text

def query(search, num=1, stemmed_pages_path=STEMMED_PAGES) :
    stoplist = stopwords.words('english')
    stemmer = SnowballStemmer('english')
    lt_search = [stemmer.stem(word) for word in search.lower().split() if word not in stoplist]
    result = list()
    matched_words = dict()
    
    for file_ in fileNames(stemmed_pages_path) :
        text = read(file_)
        tokens = text.split()
        countWords = len(tokens)
        for word in lt_search : matched_words[word] = 0
        
        for token in tokens :
            if (token in lt_search) :
                matched_words[token] += 1
        
        non_zero = list(filter(lambda x: x != 0, matched_words.values()))
        matched_words_count = len(non_zero)
        matched_words_overall = reduce(lambda x,y: x+y, matched_words.values())
        score = matched_words_count + matched_words_overall / countWords
        result.append((file_.split('/')[-1].replace('_',' '), score))
    result = sorted(result, key=lambda item : -item[1])
    
    if (num == 1) :
        return result[0][0]
    return result[:num]

if __name__ == "__main__":
    print(query("buy clothes", 10))
