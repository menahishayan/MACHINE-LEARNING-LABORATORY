# -*- coding: utf-8 -*-
"""p6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1egnOJYXJNN3uzioh5ZtgSq6FSj2dDscq
"""

from sklearn.datasets import fetch_20newsgroups

categories = ['alt.atheism','comp.graphics', 'sci.med']
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True)
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True)

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

cv, tfidf = CountVectorizer(), TfidfTransformer()

X_train_tfidf = tfidf.fit_transform(cv.fit_transform(twenty_train.data))
y_train = twenty_train.target

X_test_tfidf = tfidf.transform(cv.transform(twenty_test.data))
y_test = twenty_test.target

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

mnb = MultinomialNB()
mnb.fit(X_train_tfidf, y_train)

y_pred = mnb.predict(X_test_tfidf)

print(classification_report(y_test, y_pred, target_names=twenty_test.target_names))
