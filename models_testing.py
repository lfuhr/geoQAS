import word2vec
import wiki_match
import free_dict
import questionsModelTest

def printResult(key, count, questions) :
    print(key + " - " + str(count[key][True]) + " " + str(count[key][False]) + " " + str(round(count[key][True] / questions * 100,1)) + "%")

count = dict()
count["wikimatch"] = {True: 0, False: 0}
count["freeDict"] = {True: 0, False: 0}
count["word2vec"] = {True: 0, False: 0}
questions = len(questionsModelTest.questionsModelTest)
for (question,answer) in questionsModelTest.questionsModelTest:
	word2vecvalue=word2vec.query(question,1)
	count["word2vec"][word2vecvalue.lower() == answer] += 1
	wikivalue=wiki_match.query(question,1)
	count["wikimatch"][wikivalue == answer] += 1
	#freedictvalue=free_dict.query(question,1)
	freedictvalue=wiki_match.query(question,1,'common_knowledge/dict_pages/stemmed') # should be more accurate as the free_dict query
	count["freeDict"][freedictvalue == answer] += 1
	
	print(question + " - " + answer)
	print("word2vec  - "+word2vecvalue)
	print("wikimatch - "+wikivalue)
	print("freeDict  - "+freedictvalue+"\n")
		
print("Results:")
printResult("word2vec", count, questions)
printResult("wikimatch", count, questions)
printResult("freeDict", count, questions)
