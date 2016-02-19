import os
import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from collections import defaultdict

SOURCE_PATH = 'full'
DESTINATION_PATH = 'stemmed/'

# Reads all filenames contained by the root directory
def fileNames(root) :
    names = []
    for root, dirs, files in os.walk(root) :
        for file_ in files :
            names.append(root + '/' + file_)
    return names

# Reads a file
def read(f_path) :
    f = open(f_path, 'r', encoding='utf8', errors='replace')
    text = f.read()
    f.close()
    return text

# Formats the text as words separated by spaces
def format_text(text) :
    text = ' '.join(text.split('\n')) # remove new lines
    chars = ['.',',',':','?','!','"','(',')','[',']','{','}','=',';','-']
    for char in chars :
        text = text.replace(char, '')
    return text

# Remove stopwords and stems remaining words
def removeAndStemWords(text) :
    stoplist = stopwords.words('english')
    stemmer = SnowballStemmer('english')
    texts = [stemmer.stem(word) for word in text.lower().split() if word not in stoplist]
    return texts

def save(name, stemmed) :
    if not os.path.exists(DESTINATION_PATH) :
        os.makedirs(DESTINATION_PATH)
    file_ = open(DESTINATION_PATH + name.split('/')[1], 'w+')
    file_.write(' '.join(stemmed))
    file_.close()   

names = fileNames(SOURCE_PATH)
for name in names :
    text = read(name)
    formatted = format_text(text)
    stemmed = removeAndStemWords(formatted)
    save(name, stemmed)
