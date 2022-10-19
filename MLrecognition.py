import csv

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier


def prediction(TextExtracted):
    if TextExtracted =='':
        print('No text detected. Try to take a better picture or with more light.')
    else:
        # transfère du doc csv
        df = pd.read_csv('language-identification-datasets.csv')

        # division en 2 array pour text et langue
        x = df['Text']
        y = df['Language']
        x_train = x[0:24326]
        y_train = y[0:24326]
        x_test = TextExtracted

        # classifier
        pipeline = Pipeline([('vect', CountVectorizer()), ('clf', DecisionTreeClassifier())])
        pipeline.fit(x_train, y_train)
        prediction = pipeline.predict([x_test])
        print("The language used in this text is " + str(prediction))
