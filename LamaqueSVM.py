# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 11:02:28 2015

@author: lorenzoperozzi
"""

import numpy as np
from sklearn.cross_validation import train_test_split
import pandas as pd
import random
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

folder = 'data'
# Categorical dataset
lamaque = pd.read_csv(folder+'/lamaque_processed_categories.csv')

rows = random.sample(lamaque.index, int(len(lamaque)))
lamaque = lamaque.ix[rows]

#SVM analysis
X = lamaque.as_matrix(columns=['X','Y','Z','DISTANCE_TO_FAULT','DISTANCE_TO_DIORITE','DISTANCE_TO_GRANODIORITE','DISTANCE_TO_GLD'])

Y = lamaque['AU_CLASS_CAT'].values.tolist()
Y = np.asarray(Y)

X_train , X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=42)

clf = SVC()
clf.fit(X_train, Y_train)

# errors on test set & sparsity
svc_error = np.sum(Y_test!=clf.predict(X_test)) / len(Y_test)
Y_pred = clf.predict(X_test)
accuracy_score = accuracy_score(Y_test, Y_pred)
svc_message = "SVC prediction error on test set for lamaque dataset is {0}"
print svc_message.format(accuracy_score)