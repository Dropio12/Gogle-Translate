import csv

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


def prediction(TextExtracted):
    if TextExtracted =='':
        print('No text detected. Try to take a better picture or with more light.')
    else:
        # transfère du doc csv
        df = pd.read_csv('dataset.csv')

        # division en 2 array pour text et langue
        x = df['Text']
        y = df['language']
        #x_train = x[0:24326]
        #y_train = y[0:24326]
        x_test = TextExtracted
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=3)
        # classifier
        model = Pipeline([('vect', CountVectorizer()), ('clf', DecisionTreeClassifier())])
        model.fit(X_train, y_train)
        #prediction
        print(model.score(X_test, y_test))
        prediction = model.predict([x_test])
        print("The language used in this text is " + str(prediction))
