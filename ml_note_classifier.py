from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle

Sample training data

texts = [
"Python loops and functions",
"Machine learning and neural networks",
"Database SQL queries",
"Calculus differentiation formulas",
"Artificial intelligence and automation",
"HTML CSS web design",
"Statistics and probability",
"Deep learning models"
]

labels = [
"Programming",
"AI",
"Database",
"Math",
"AI",
"Web Development",
"Math",
"AI"
]

Create ML pipeline

model = Pipeline([
('tfidf', TfidfVectorizer()),
('classifier', MultinomialNB())
])

Train model

model.fit(texts, labels)

Save model

with open("note_classifier.pkl", "wb") as file:
pickle.dump(model, file)

print("AI Note Classification Model Trained Successfully!")
