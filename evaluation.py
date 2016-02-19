import main
import qadictionary

def getEvaluationForTesting():
	rightresult=0
	errorresult=0
	wrongresult=0
	print("Evaluation for questions used for testing:")
	for key, value in qadictionary.question_testing.items():
		try:
			queryvalue=main.answer_question(key).replace("\n", "")
			value=value.replace("\n", "")
			if value.replace(" ", "")==queryvalue.replace(" ", ""):
				rightresult=rightresult+1
				#print("right answer - "+key+"\nReturn results:"+queryvalue+"\nReal results:"+value+"\n\n")
			else:
				wrongresult=wrongresult+1
				#print("wrong answer - "+key+"\nReturn results:"+queryvalue+"\nReal results:"+value+"\n\n")
		except:
			errorresult=errorresult+1
			#print("error in query - "+key+"\n"+value+"\n\n")
			

	print("number of right questions answered:"+str(rightresult))
	print("number of wrong questions answered:"+str(wrongresult))
	#print("number of error in queries:"+str(errorresult))
	precision=(rightresult/(rightresult+wrongresult))*100
	print("precision :"+str(precision)+"%")

def getEvaluationForTraining():
	rightresult=0
	errorresult=0
	wrongresult=0
	print("Evaluation for questions used for training:")
	for key, value in qadictionary.result_testing_training.items():
		try:
			queryvalue=main.answer_question(key).replace("\n", "")
			value=value.replace("\n", "")
			if value.replace(" ", "")==queryvalue.replace(" ", ""):
				rightresult=rightresult+1
				#print("right answer - "+key+"\nReturn results:"+queryvalue+"\nReal results:"+value+"\n\n")
			else:
				wrongresult=wrongresult+1
				#print("wrong answer - "+key+"\nReturn results:"+queryvalue+"\nReal results:"+value+"\n\n")
		except:
			errorresult=errorresult+1
			#print("error in query - "+key+"\n"+value+"\n\n")
			

	print("number of right questions answered:"+str(rightresult))
	print("number of wrong questions answered:"+str(wrongresult))
	#print("number of error in queries:"+str(errorresult))
	precision=(rightresult/(rightresult+wrongresult))*100
	print("precision :"+str(precision)+"%")

if __name__ == "__main__":
	getEvaluationForTraining()
	getEvaluationForTesting()

