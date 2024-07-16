# src/models/topic_classifier.py
from transformers import pipeline

class TopicClassifier:
    def __init__(self):
        self.classifier = pipeline("zero-shot-classification")

    def classify_topic(self, text, candidate_labels):
        try:
            result = self.classifier(text, candidate_labels)
            return result
        except Exception as e:
            print(f"Error: {e}")
            return str(e)
