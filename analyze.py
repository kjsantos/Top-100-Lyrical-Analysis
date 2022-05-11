import vaderSentiment as vader
import csv
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
import datetime
from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



with open ('collected_dataset.csv', 'r+', encoding='utf-8') as file:
	df= pd.read_csv(file, header=0, index_col=[0])

df = df.dropna(subset=['lyrics'])


pos = []
neu = []
neg = []
comp = []
cl = []
analyzer = SentimentIntensityAnalyzer()


new_words = df['lyrics']

stop_words = set(stopwords.words('english'))

for line in new_words:

    tokenizer = RegexpTokenizer(r'\w+')
    word_tokens = tokenizer.tokenize(line)

    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

    filtered_sentence = []
    new_string = ""

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w.lower())

    for word in filtered_sentence:
        new_string = new_string + word + " "

    vs = analyzer.polarity_scores(new_string)
    pos.append(vs['pos'])
    neu.append(vs['neu'])
    neg.append(vs['neg'])
    comp.append(vs['compound'])
    if (vs['compound'] > .05):
        cl.append('Positive')
    elif (vs['compound']< (-.05)):
        cl.append('Negative')
    else:
        cl.append('Neutral')
df['Positive Score'] = pos
df['Neutral Score'] = neu
df['Negative Score'] = neg
df['Overall Sentiment Score'] = comp
df['General Feeling'] = cl

df.to_pickle("withsent.pkl")
df.to_csv('final_dataset.csv')

print(df)



