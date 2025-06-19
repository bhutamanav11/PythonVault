from textblob import TextBlob
from autocorrect import Speller
spell = Speller(lang='en')

text = "I love progamming and machine learnig."
print("Original Text: ",text)
print("Speller corrected text: ",spell(text))
blob = TextBlob(text)
correct = blob.correct()
print("original text: ",text)
print("Corrected text using TextBlob: ",correct)