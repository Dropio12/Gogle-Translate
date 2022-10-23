import csv
import re

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
from NumberRemoverForText import remove_number_text


def prediction(TextExtracted):
    if TextExtracted == '':
        print('No text detected. Try to take a better picture or with more light.')
    else:
        # transfer du doc csv
        df = pd.read_csv('language-identification-datasets.csv')
        # division en 2 array pour text et language
        x = df['Text']
        y = df['Language']
        X_train = x[0:24326]
        y_train = y[0:24326]

        #df.apply(
           # lambda row: main_contraction(row["Text"]) if row["Language"] == "English" else row["Text"], axis=1)
       # x.apply(remove_number)
        #x.apply(remove_URL)
        #df.apply(
        #    lambda row: remove_emoji(row["Text"]) if row["Language"] == "English" else row["Text"], axis=1)
       # df.apply(
       ##     lambda row: other_clean(row["Text"]) if row["Language"] == "English" else row["Text"], axis=1)

        x_test = TextExtracted
        x_test = remove_number_text(x_test)
        print(x_test)
        x_test = remove_URL(x_test)
        print(x_test)
        x_test = remove_emoji(x_test)
        print(x_test)
        # if x_test has contractions or maj or other things, switch them **********
        x_test = to_lower(x_test)
        print(x_test)
        x_test = other_clean(x_test)
        print(x_test)
        x_test = [x_test]

        model = Pipeline([('vect', CountVectorizer()), ('clf', DecisionTreeClassifier())])
        model.fit(X_train, y_train)
        x_prediction = model.predict(x_test)
        print("The language used in this text is " + str(x_prediction))


prediction("Hey, what is going on my friend? It's been a long timse since 123")
