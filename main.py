'''
Launches an interactive Shell for posing quesitons
'''
import nltk
import questions
import chunking
import query_creator
import database
import classifier
import precise; from precise import *
import sys


## Reads a question from the input. If a number from 1 to 20 is used, the corresponding test question is used.
def read_question() :

    question = input("Please enter your question: \n(Note: Test questions are used if it is a number from 1 to " + str(len(questions.targetquestions)) + ")\n")

    try :
        question_num = int(question)
    except ValueError:
        return question
    
    if (int(question) in range(1,len(questions.targetquestions)+1)) :
        question = questions.targetquestions[int(question) - 1]
        print("Use question: '" + question +"'")
        
    return question


def print_result(output) :
    if (len(output) == 0) :
        print("No result found in dataset!\n")
    else :
        print(output + "\n")

def format_result(json_data) :
    output = ""
    
    if ('boolean' in json_data.keys()) :
        # example result: {'boolean': True, 'head': {'link': []}}
        output = str(json_data["boolean"])
    else :
        for result in json_data["results"]["bindings"]:
            if (len(output) > 0) :
                output += "\n"
            for var in json_data["head"]["vars"]:
                if (var in result) :
                    output += result[var]["value"] + " "
    return output

# Answers a question string and returns the text result as a multiline string.
def answer_question(question) :

    # chunk question
    chunked_question = chunking.Question(question)
    
    # formalize the chunks
    precise_question = Precise(chunked_question)

    # select query
    query = query_creator.create_query(precise_question)

    #print("\n" + query + "\n")

        
    # run query
    result = database.execute(query)

    if debug:
        print("POStagged : " + str(chunked_question.tagged)) 
        print("Chunked   : " + str(chunked_question.chunked))
        print("Answertype: " + str(precise_question.answertype))
        print("Attribute : " + str(precise_question.attribute))
        print("Subject   : " + str(precise_question.subject))
        print("Properties: " + str(precise_question.properties))
        print()
        print("Answer")

    # read and format result
    return format_result(result)

debug = len(sys.argv) > 1 and sys.argv[1] == 'd'

if __name__ == "__main__":
    
    # Ask for questions as long as the user does not type 'q', 'quit', 'e' or 'exit'
    quit = False
    while not quit :
        
        # read in question from command line
        question = read_question()
        if question in {"q", "quit","e","exit"}:
            quit = True
            break;
        
        # answer the question
        try :
            result = answer_question(question)
            
            # print result
            print_result(result)
            
        # catch RuntimeErrors like "no IRI found for noun" etc. to continue with input loop
        except Exception as e:
            print("RuntimeError occured, program aborted:")
            print(str(e) + "\n")

