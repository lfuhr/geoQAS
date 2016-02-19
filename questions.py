"""
Different sets of questions.
 - targetquestions: trainingset
 - testset
 - original questions including events
"""
targetquestions = [
    "Are there any dentists near me?",
    "How far away is Padu from my home?",
    "How far away is Passau from Berlin?",
    "How far away is Universität Passau from Padu?", #duplicate
    "How far away is the closest supermarket to Universität Passau?", 
    "How far is Passau from Munich?", #Missing Translation
    "How long does it take to go from Innstraße 33 Passau to Löwengrube 10?", #No result found in dataset!-- needs Work
    "How many eateries are in Passau?", #duplicate
    "How many restaurants are in Passau?",
    "How many streets does Passau have?",
    "Is the Klinikum Passau located in Innstraße?",
    "Is the Universität Passau located in Innstraße?", #Wrong
    "Is there a cinema near a bar in Passau?",
    "Is there a hospital in Passau?", 
    "Is there an airport in Passau?", #Wrong
    "List me all museums in Passau?",
    "What is the address of Padu?",
    "What is the distance between Padu and Bayerischer Löwe",
    "What is the distance between Padu and Innbräu", #duplicate
    "What is the distance between Padu and me",#duplicate
    "What is the distance to Padu?",
    "What is the distance to the closest Italian restaurant from Universität Passau?",
    "What is the distance to the closest Italian restaurant?",#duplicate
    "What is the nearest city from Passau?",
    "What is the nearest pharmacy?",
    "Where is Ludwigsplatz?", #No Result
    "Where is Padu in Passau?",
    "Where is Residenzplatz?", # Salzburg
    "Where is the castle in Passau?",
    "Where is the touristic castle in Passau?", # No Result
    "Which attractions are in Passau?",
    "Which restaurants are in Passau?",
    "Which supermarkets are in a range of 1 km from my home?",
    "Which types of restaurants are there in Passau?",
    "What is the closest parking to Klinikum Passau?", #Code 500
    "What is the closest supermarket to Universität Passau?",
    "Which attractions can I visit in Passau?",

    #word2vec
    "Where can I park my car in Passau?",
    "Where can I eat ice cream in Passau?", #There is none
    "Where can I eat ice cream in München?",
    "Where can I find an Italian restaurant in Passau?",
    "Where can I repair my mobile phone in Passau?", #No class found for 'shoe shop'-------------- needs Work
    "Where can I go swimming in Passau?",
]

# Created by an independent Person
testset = [
   "Where is the tourist information located?",
   "How far is to the next patrol station? /gas station?",
   "Where can i find a free parking area?",
   "Is there a basement car park in the city center of Passau?",
   "How many youth hostels are in Passau?",
   "Is there a hotel near the central station?",
   "Where is the closest parking lot to the central station?",
   "Which parink lot is closest to the central station?",
   "How many schools can I find in Passau?",
   "Where is the next school?",
   "Is there a cafe in öldenpeterweg?",
   "Where can I find a laundromat?",
   "How far is the next ATM?",
   "Where is the closest ATM?",
   "Is there a ice cream parlor in Innstadt?",
   "Is there a petrol station in the south of Passau?",
   "Which is the closest cafe to the university?",
   "Where is a open barber shop?",
   "How long does it take to get from Passau to Hauzenberg?",
   "Which rivers are in passau?",
]

original = [
    "How many restaurants has Passau?",
    "How long does it take to go from Innstraße 33 Passau to Löwengrube 0",
    "How many supermarkets are opened now?",
    "Is the University of Passau located in Innstraße?",
    "What is the next event in Scharfrichterhaus?",
    "What events take place at 20:00?",
    "What is the nearest city from Passau?",
    "What is the address of the University of Passau?",
    "Where is Ludwigsplatz (in Passau)?",
    "Where can I find an italian restaurant in Passau?",
    "Is there a hospital?",
    "How far away is the closest supermarket?",
    "Which clubs have opened today?",
    "Is there a cinema near a bar?",
    "Which supermarkets are in a range of 1 km from my home?",
    "Which types of restaurants are there in Passau?",
    "How many streets has Passau?",
    "Where does Campusfest take place?",
    "Where can I park my car?",
    "When has Marienbrücke been built?",
]
