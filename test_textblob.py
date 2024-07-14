from textblob import TextBlob

texts = [
    "The team's hard work paid off, and we won the competition.",  # Positive
    "I am very happy today because my project went well.",  # Positive
    "I am very unhappy with the current situation and feel hopeless.",  # Negative
    "The weather is cloudy today and I plan to stay home all day."  # Neutral
]

for text in texts:
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    print(f"Text: {text}")
    print(f"Sentiment Polarity: {sentiment}")
    if sentiment > 0:
        print("Sentiment: Positive")
    elif sentiment < 0:
        print("Sentiment: Negative")
    else:
        print("Sentiment: Neutral")
    print()
