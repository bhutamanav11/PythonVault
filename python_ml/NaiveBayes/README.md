````markdown
# 🧠 NLP Practice Summary – Codedex GenAI

This repository contains my hands-on practice and learning from the **Codedex GenAI NLP Tutorial**. I explored core Natural Language Processing (NLP) concepts using Python libraries like **NLTK**, **TextBlob**, **Autocorrect**, and more.

---

## ✅ Topics Covered

### 1. **NLTK Basics**
- Installed and used `nltk` library
- Downloaded required data packages (`punkt`, etc.)
- Learned how to preprocess and clean text

---

### 2. **Tokenization**
- Used `nltk.word_tokenize()` to split text into words
- Applied sentence tokenization and word tokenization

```python
from nltk.tokenize import word_tokenize
tokens = word_tokenize("this is a sample sentence")
````

---

### 3. **N-Grams**

* Generated bigrams and trigrams using NLTK
* Understood how N-grams can be used in language modeling

```python
from nltk import ngrams
list(ngrams(tokens, 2))  # Bigrams
```

---

### 4. **Naive Bayes Text Classification**

* Used `CountVectorizer` to vectorize text
* Built classifiers using `MultinomialNB`
* Predicted categories like **tech vs non-tech** and **positive vs negative**
* Measured accuracy with `accuracy_score`

---

### 5. **Translation**

* Used the `translate` library to convert text into other languages
* Tried out Hindi (`hi`) and Gujarati (`gu`) translations

```python
from translate import Translator
Translator(to_lang="hi").translate("hello world")
```

---

### 6. **Text Correction with TextBlob**

* Corrected grammar and spelling using `TextBlob`

```python
from textblob import TextBlob
TextBlob("i am in leov with competers").correct()
```

---

### 7. **Autocorrect Library**

* Fixed spelling errors using the `autocorrect` package

```python
from autocorrect import Speller
spell = Speller(lang='en')
spell("this moovie is grreat")
```

---

## 📌 Summary

Throughout this GenAI-powered Codedex NLP module, I learned:

* Core NLP building blocks
* How to preprocess, clean, and analyze text
* How to build basic ML models for classification
* Real-world applications of NLP like translation and spell correction

---

### 👨‍💻 Author

**Manav Bhuta**
Computer Engineering Student
Mumbai, India

```
