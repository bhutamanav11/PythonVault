import nltk 
# nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
sample_text = "I am learning NLP(Natural Language Processing)"
tokens = word_tokenize(sample_text)
unigram = list(ngrams(tokens,1))
print('unigram',unigram)
bigram = list(ngrams(tokens,2))
print('bigram',bigram)
trigram = list(ngrams(tokens,3))
print('trigram',trigram)

# print('tokens: ',tokens)