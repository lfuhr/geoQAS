Requirements:
- python 3 (because of umlaut)
- java 8 for stanford-postagger
- setuptools (python package, is included in pip3 installation)
- nltk + downloaded books (nltk will be installed automatically, however books have to be downloaded using nltk.download() )


Installation:
- Run setup.py: python3 setup.py install
- Maybe sudo is required


Configuration
-Different Pararmeters are availible in conf.py


Python scripts that can run on its own.
- main application:   main.py
- main evaluation:    evaluation.py
  based on testset


Sets of Questions in questions.py
- original
- trainingset alias targetquestions
- testset


Common knowledge
We use two approaches for common knowledge
- Looking up in Wikipedia / thefreedictionary  → located in folder common_knowledge
- Using word2vec


The Tagset used by NLTK is the one from penn treebank. We exteded it with INO, for the preposition "of"
Original
1.	CC	Coordinating conjunction
2.	CD	Cardinal number
3.	DT	Determiner
4.	EX	Existential there
5.	FW	Foreign word
6.	IN	Preposition or subordinating conjunction
7.	JJ	Adjective
8.	JJR	Adjective, comparative
9.	JJS	Adjective, superlative
10.	LS	List item marker
11.	MD	Modal
12.	NN	Noun, singular or mass
13.	NNS	Noun, plural
14.	NNP	Proper noun, singular
15.	NNPS	Proper noun, plural
16.	PDT	Predeterminer
17.	POS	Possessive ending
18.	PRP	Personal pronoun
19.	PRP$	Possessive pronoun
20.	RB	Adverb
21.	RBR	Adverb, comparative
22.	RBS	Adverb, superlative
23.	RP	Particle
24.	SYM	Symbol
25.	TO	to
26.	UH	Interjection
27.	VB	Verb, base form
28.	VBD	Verb, past tense
29.	VBG	Verb, gerund or present participle
30.	VBN	Verb, past participle
31.	VBP	Verb, non-3rd person singular present
32.	VBZ	Verb, 3rd person singular present
33.	WDT	Wh-determiner
34.	WP	Wh-pronoun
35.	WP$	Possessive wh-pronoun
36.	WRB	Wh-adverb
