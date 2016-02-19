import word2vec
import wiki_match
import free_dict
import questionsModelTest


for question in questionsModelTest.questionsModelTest:
	#try:
		word2vecvalue=word2vec.query(question,1)
		wikivalue=wiki_match.query(question,1)
		freedictvalue=free_dict.query(question,1)
		print(question+"\n")
		print("word2vec  - "+word2vecvalue+"\n")
		print("wikimatch - "+wikivalue+"\n")
		print("freeDict  - "+freedictvalue+"\n")
	#except Exception as e:
	#	print("error in query - "+question+str(e)+"\n")
		


