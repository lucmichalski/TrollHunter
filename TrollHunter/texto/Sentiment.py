from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import pandas as pd


def get_sentiment_from_tweets(tweet):
    analyser = SentimentIntensityAnalyzer()
    sentiment_scores = []

    for t in tweet:
        score = analyser.polarity_scores(t)
        score['tweet'] = t
        sentiment_scores.append(score)

    sentiment_df = pd.DataFrame(sentiment_scores)

    return sentiment_df


def get_polarity(tweet):
    tab_result = {'tweet': [],
                  'polarity': []}

    for t in tweet:
        obj = TextBlob(t)
        polarity = obj.sentiment.polarity

        tab_result['tweet'].append(t)
        tab_result['polarity'].append(polarity)

    df_result = pd.DataFrame(tab_result, columns=['tweet', 'polarity'])

    return df_result


if __name__ == '__main__':
    tweets = ["I'm so happy", "I surprised him", "It's a sad news", "I'm happy and sad at the same time"]
    result = get_polarity(tweets)

    print(result)
