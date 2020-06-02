from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer= SentimentIntensityAnalyzer()

pos_count=0
pos_correct =0
neg_count=0
neg_correct=0
with open("aspirn.txt","r") as f:
    for line in f.read().split('\n'):
        vs=analyzer.polarity_scores(line)
        print("{}{}".format(line,str(vs)))
        print("\n")
        if vs['compound']>0:
            pos_correct+=1
        pos_count+=1
        if vs['compound']<=0:
            neg_correct+=1
        neg_count+=1

print("Positive accuracy={}% via {} samples".format(pos_correct/pos_count*100.0,pos_count))

print("Negative accuracy={}% via {} samples".format(neg_correct/neg_count*100.0,neg_count))
