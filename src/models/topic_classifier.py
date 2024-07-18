# src/models/topic_classifier.py
# این فایل برای طبقه‌بندی موضوعات متن استفاده می‌شود

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

class TopicClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.classifier = MultinomialNB()
        self.model_path = 'path/to/your/model.pkl'  # مسیر به مدل ذخیره‌شده

    def train(self, texts, labels):
        X = self.vectorizer.fit_transform(texts)
        self.classifier.fit(X, labels)
        with open(self.model_path, 'wb') as f:
            pickle.dump((self.vectorizer, self.classifier), f)

    def classify(self, text):
        with open(self.model_path, 'rb') as f:
            self.vectorizer, self.classifier = pickle.load(f)
        X = self.vectorizer.transform([text])
        prediction = self.classifier.predict(X)
        return prediction[0]
