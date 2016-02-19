from __future__ import division
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import os

STEMMED_PAGES = 'common_knowledge/dict_pages/stemmed'

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

def query(search, num=1) :
    stoplist = stopwords.words('english')
    stemmer = SnowballStemmer('english')
    lt_search = [stemmer.stem(word) for word in search.lower().split() if word not in stoplist]
    result = list()
    for file_ in fileNames(STEMMED_PAGES) :
        text = read(file_)
        tokens = text.split()
        countWords = len(tokens)
        countHits = 0
        for token in tokens :
            if (token in lt_search) :
                countHits += 1
        result.append((file_.split('/')[-1].replace('_',' '), countHits / countWords))
    result = sorted(result, key=lambda item : -item[1])
    
    if (num == 1) :
        return result[0][0]
    return result[:num]

if __name__ == "__main__":
    print(query("buy clothes", 10))
