"""
Questions and answers for automatic testing.
"""

result_testing_training = {
    "Are there any dentists near me?":"True", #train
    "How far away is Padu from my home?": "0.183972 1.21554 1441.27",  #train
    "How far away is Passau from Berlin?":"557,6377", #train
    "How far away is the closest supermarket to Universität Passau?": "0.461794",  #train
    "How many restaurants are in Passau?": "68",  #train
    "Is the Klinikum Passau located in Innstraße?":"True",  #train
    "Is there a hospital in Passau?": "True",  #train
    "What is the address of Padu?": "Padu Innstraße 46 Padu Höllgasse 24", #train
    "What is the distance between Padu and Innbräu":"0.734567 1.27156 1440.32",  #train
    "What is the distance to the closest Italian restaurant from Universität Passau?":"0.855996 ", #train
    "What is the nearest city from Passau?":"Linz", #train
    "What is the nearest pharmacy?":"Nikola-Apotheke", #train
    "Which attractions are in Passau?":"", #train
    "Which supermarkets are in a range of 1 km from my home?":"Edeka Naturkost Buck REWE",#train
    "What is the closest supermarket to Universität Passau?":"Edeka", #train
    "Is there an airport in Passau?": "False", #Wrong 
    "Where is the closest ATM?":"ATM 45.4891 15.5472",#train
    "Where can I go swimming in Passau?":"Halser Stausee 48.5901 13.4576",#train
    "What is the distance to the closest Italian restaurant?":"0.855996 ",#train
    "How many schools can I find in Passau?":"27",
}

question_testing={
    "How far away is Universität Passau from Padu?": "0.183972 1.21554 1441.27", 
    "How far is Passau from Munich?": "192,4 km", #Missing Translation 
    "How long does it take to go from Innstraße 33 Passau to Löwengrube 10?":"",  #No result found in dataset!-- needs Work
    "How many eateries are in Passau?":"68", 
    "Which attractions can I visit in Passau?":"",#train
    "Is the Universität Passau located in Innstraße?":"True",  #Wrong 
    "What is the distance between Padu and Bayerischer Löwe":"191.145 191.989 1562.02 ",
    "What is the distance between Padu and me":"0.183972 1.21554 1441.27 ",
    "What is the distance to Padu?":"0.183972 1.21554 1441.27 ",
    "Where is Padu in Passau?": "Padu Innstraße 46 48.5696 13.4548 Padu Höllgasse 24 48.5758 13.4654",
    "Where is the touristic castle in Passau?": "Oberhaus 48.578403 13.471458", 
    "Which restaurants are in Passau?":"Akropolis Athen Altes Bräuhaus Am Paulusbogen Bayerisch Venedig Bayerischer Löwe Beef Boys Bilancia d’Oro Biogasthof Stelzlhof Blaas Blauer Bock Bollywood Bongusto Burgwald CallaPizza Cantina Ensenada Chandni Croatia Da Franco Del Padrone Gailberghöhe Gallo Nero Gasthof 3 Linden Gasthof Apfelkoch Gasthof Edelweiss Golden Wok Goldenes Schiff Innbräu Kirchenwirt Engl Korfou Leonardo Mandarin Margaritas Mariandl Mondo Italiano Nibelungen-Stüberl PADU Bistro Padu Park Cafe Pata Negra Pension zur Brücke Peschl-Terrasse Pizza Roma Ratskeller Restaurant & Landhaus Kellerwand Restaurant Huber Feistritzer Restaurant Reiter Rhodos Rive Gauche Rosencafe Aschenbrenner Rusticana Salzweger Hof Scharfrichterhaus Sensasian Sportgaststaette Hacklberg Venti Tre Vogl Waldschloss Weinbeißer Wirt z´Moarhof Wok of Fame Zi Teresa Zum Grünen Baum Zum Tiroler Zur Löwmühle Zur Triftsperre Ödenhütte",
    "Which types of restaurants are there in Passau?":"asian asian;wok bavarian chinese french greek indian italian mexican pizza regional seafood;steak_house ",
    "What is the closest parking to Klinikum Passau?":"ParkHause Innstraße 71", #Code 500
    "How many youth hostels are in Passau?":"1",
    "How many schools can I find in Passau?":"27",
    "Where is the castle in Passau?" : "Oberhaus 48.578403 13.471458", #train
    "Where can I find an Italian restaurant in Passau?":"Bilancia d’Oro Residenzplatz 6 48.5741 13.4675 CallaPizza 48.5735 13.4621 Del Padrone 48.5755 13.4574 Mondo Italiano 48.5758 13.4596 Padu Höllgasse 24 48.5758 13.4654 ",
<<<<<<< HEAD
    "Where can I park my car in Passau?":"",
    "Where can I eat ice cream in Passau?":"", 
}
=======

}
>>>>>>> 0fb391104e57f1110165ff3719796498a4aa97a5
