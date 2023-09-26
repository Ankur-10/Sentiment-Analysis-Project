from textblob import TextBlob


sentences = []
for i in range(5):
    sent = input()
    sentences.append(sent)

for sentence in sentences:
    blob = TextBlob(sentence)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    print(f"Sentence: '{sentence}'")
    print(f"Sentiment: {sentiment} (Polarity: {polarity:.2f}, Subjectivity: {subjectivity:.2f})")
    print()
