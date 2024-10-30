import spacy

nlp = spacy.load("en_core_web_sm")
sentence = input("Input a sentence:\n")

doc = nlp(sentence)

keywords = [token.text for token in doc if token.pos_ == "NOUN"]

print(keywords) 