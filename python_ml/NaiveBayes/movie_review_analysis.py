from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# # dataset 
reviews = [
    "this moovie was a masterpeece.",
    "absolutely luvd the charactrs and story.",
    "briliant direction and stuning visuals.",
    "the soundtrak was really tuching.",
    "great performence by the leed actor.",
    "i enjoied evry moment of the film.",
    "the plot twist was unexpcted and smrat.",
    "well-pased and emtionally engaging.",
    "the cinematgraphy was beautful.",
    "a heartwaming and memrable moovie.",

    "this moovie was a total dissapointment.",
    "the storry made no sence at all.",
    "acting was falt and boring.",
    "i regret wasting my tyme on this.",
    "poorr script and terible dialog.",
    "completely predictble and dul.",
    "the editng was realy bad.",
    "not wurth watching again.",
    "charactrs were underdevloped.",
    "i nearly fel asleep halfway through."
]
labels = [
    "positive", "positive", "positive", "positive", "positive",
    "positive", "positive", "positive", "positive", "positive",
    "negative", "negative", "negative", "negative", "negative",
    "negative", "negative", "negative", "negative", "negative"
]


# reviews = ['This movie was fantastic! A must-watch.',
#            'I didn\'t enjoy this movie at all.',
#            'Amazing storyline and great acting!',
#            'The plot was dull and predictable.',
#            'Loved the cinematography! Highly recommended.']

# labels = ['positive', 'negative', 'positive', 'negative', 'positive']
# vectorizing the dataset
from autocorrect import Speller
spell = Speller(lang='en')
corrected_rev = [spell(review) for review in reviews]
for original, corrected in zip(reviews, corrected_rev):
    print("Original: ", original)
    print("Corrected:", corrected)
    print()
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(corrected_rev)
# split data into training and testing data
x_train , x_test , y_train , y_test = train_test_split(x,labels,test_size=0.1,random_state=42)
#create a naive bayes model
model = MultinomialNB()
model.fit(x_train,y_train)
#predict values based on testing data
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test,y_pred)
#printing actual reviews and predicted reviews
print("Actual reviews answer for test data: ",y_test)
print("Predicted reviews answer for test data: ",y_pred)
#accuracy
print("Accuracy of the model",accuracy)
if accuracy>0.5:
    print("Good Vibes,Book the ticket right now!")
else:
    print("Don't Book the ticket")

# #CV accuracy
# from sklearn.model_selection import cross_val_score
# scores = cross_val_score(model, x, labels, cv=5)
# print("CV Accuracy:", scores.mean()*100)
