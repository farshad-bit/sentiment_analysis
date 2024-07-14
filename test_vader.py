<<<<<<< HEAD
# test_vader.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

texts = [
    "The team's hard work paid off, and we won the competition.",  # Positive
    "I am very happy today because my project went well.",  # Positive
    "I am very unhappy with the current situation and feel hopeless.",  # Negative
    "The weather is cloudy today and I plan to stay home all day."  # Neutral
]

analyzer = SentimentIntensityAnalyzer()

for text in texts:
    sentiment = analyzer.polarity_scores(text)
    compound = sentiment['compound']
    print(f"Text: {text}")
    print(f"Sentiment Compound: {compound}")
    if compound > 0.05:
        print("Sentiment: Positive")
    elif compound < -0.05:
        print("Sentiment: Negative")
    else:
        print("Sentiment: Neutral")
    print()
=======
# test_vader.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

texts = [
    "The team's hard work paid off, and we won the competition.",  # Positive
    "I am very happy today because my project went well.",  # Positive
    "I am very unhappy with the current situation and feel hopeless.",  # Negative
    "The weather is cloudy today and I plan to stay home all day."  # Neutral
]

analyzer = SentimentIntensityAnalyzer()

for text in texts:
    sentiment = analyzer.polarity_scores(text)
    compound = sentiment['compound']
    print(f"Text: {text}")
    print(f"Sentiment Compound: {compound}")
    if compound > 0.05:
        print("Sentiment: Positive")
    elif compound < -0.05:
        print("Sentiment: Negative")
    else:
        print("Sentiment: Neutral")
    print()
>>>>>>> 935d61791628ea5faeb72b8363d962905dcb0289
