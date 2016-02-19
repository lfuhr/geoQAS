"""
Used by chunking.py to retrieve the answertype of a question
"""
_dict = {
    "how many" : "count",
    "give me the number" : "count",

    "what" : "value",
    "what is" : "value",
    "which" : "value",
    "list me all" : "value",

    "where can i" : "location",
    "where can i find" : "location",
    "where is" : "location",
    "where are" : "location",
    "where" : "location",

    "is" : "exists",
    "are" : "exists",
    "are there" : "exists",
    "is there" : "exists",

    "how far away is" : "distance",
    "what is the distance" : "distance",
    "how far is" : "distance",

    "when" : "time",
    
    "how long does it take": "duration",
}

def _remove_question_words(tagged, question_words) :
    words_to_remove = len(question_words.split(' '))
    return tagged[words_to_remove : ]


def calc_answertype(tagged) :
    
    # Match question words in order to detect answer type
    answer_type = ""
    question_word = ""
    words = ""
    for (word,tag) in tagged :
        words += word.lower()
        if (words in _dict) :
            question_word = words
            answer_type = _dict[question_word]
        words += " " # for seperation of words by space in next iteration
    
    if (len(answer_type) == 0) :
        raise RuntimeError("No answer type detected!")

    q_without_qword = _remove_question_words(tagged, question_word)
    
    return (question_word, answer_type, q_without_qword)
