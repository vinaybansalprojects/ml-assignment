from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser=SentimentIntensityAnalyzer()
def sentiment_analyzer_scores(sentence):
    score=analyser.polarity_scores(sentence)
    print("{}{}".format(sentence,str(score)))
sentiment_analyzer_scores(open("aspirn.txt","r"))
