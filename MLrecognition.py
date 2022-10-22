import csv

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from Contractions import main_contraction
from LowerCaracter import to_lower
from NumberRemover import remove_number
from URLRemover import remove_URL
from Abreviation_Slang import other_clean
from EmojiRemover import remove_emoji

def prediction(TextExtracted):
    if TextExtracted =='':
        print('No text detected. Try to take a better picture or with more light.')
    else:
        # transfère du doc csv
        df = pd.read_csv('language-identification-datasets.csv')
        # division en 2 array pour text et langue
        x = df['Text']
        y = df['Language']
        X_train = x[0:24326]
        y_train = y[0:24326]


        df.apply(
            lambda row: main_contraction(row["Text"]) if row["Language"] == "English" else row["Text"], axis=1)
        x.apply(remove_number)
        x.apply(remove_URL)
        df.apply(
            lambda row: remove_emoji(row["Text"]) if row["Language"] == "English" else row["Text"], axis=1)
        df.apply(
            lambda row: to_lower(row["Text"]) if row["Language"] == "English" else row["Text"], axis=1)
        df.apply(
            lambda row: other_clean(row["Text"]) if row["Language"] == "English" else row["Text"], axis=1)

        x_test = ["TextExtracted"]
        #if x_test has numbers, URL, emoji remove them **********
        x_test.apply(remove_number)
        x_test.apply(remove_URL)
        x_test.apply(remove_emoji)
        #if x_test has contractions or maj or other things, switch them **********
        x_test.apply(to_lower)
        x_test.apply(other_clean)
        print(x_test)

        model = Pipeline([('vect', CountVectorizer()), ('clf', DecisionTreeClassifier())])
        model.fit(X_train, y_train)
        prediction = model.predict(x_test)
        print("The language used in this text is " + str(prediction))


