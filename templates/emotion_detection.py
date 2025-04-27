# sentiment_analysis.py

from textblob import TextBlob

def sentiment_analysis(text):
    """
    Perform sentiment analysis on input text.
    Returns polarity and sentiment label.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Polarity is a float [-1.0, 1.0]

    # Interpret the polarity
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {
        "text": text,
        "polarity": polarity,
        "sentiment": sentiment
    }

# Example usage:
if __name__ == "__main__":
    input_text = input("Enter your text: ")
    result = sentiment_analysis(input_text)
    print(result)
