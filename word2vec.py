"""
Only for legacy. Because we use wiki_match instead.
Used for questions like "Where can i eat ice cream in Passau"
"""
from gensim.models import word2vec
from wn_dictionary import wn_lexicon
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

# Loads the word2vec model from the specified path.
MODEL = 'models/GoogleNews-vectors-negative300.bin'
print("Loading word2vec model...")
model = word2vec.Word2Vec.load_word2vec_format(MODEL, binary=True)

# Runs a similarity query on the dictionary of geo data classes and returns the best result.
def query(search, num=1) :

    stoplist = stopwords.words('english')
    stemmer = SnowballStemmer('english')
    search = [stemmer.stem(word) for word in search.lower().split() if word not in stoplist]

    result = []
    for entity in wn_lexicon.keys() :
        if (len(entity) > 0) :
            try :
                similarity = model.n_similarity(entity.lower().split(), search)
                result.append((entity, similarity))
            except KeyError :
                ""
                
    result = sorted(result, key=lambda item: -item[1])
    
    # For queries return only first result
    if (num == 1) :
        return result[0][0]
    
    # For testing purposes
    return result[:num]


# A simple test method where you can enter words to watch the results.
def test() :
    
    while True :
        search = input("Please enter your query: \n")
        print(query(search, 5))

# Run test command line application
if __name__ == "__main__":
    print(query("eat"))
    print(query("buy jeans"))
