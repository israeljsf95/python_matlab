# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 17:04:52 2020

@author: israe
"""

#brincando com Iris

import numpy as np
from sklearn.datasets import load_iris



data = load_iris()
features = data.data
feature_names = data.feature_names

target = data.target
target_names = data.target_names
labels = target_names[target]


from sklearn import tree
import graphviz

tr = tree.DecisionTreeClassifier(min_samples_leaf = 10)
tr.fit(features, labels)
tree.export_graphviz(tr, feature_names = feature_names, rounded = True, out_file = 'decision.dot')
graphviz.Source(open('decision.dot').read())

predicao = tr.predict(features)
print("Acuracia: {:.1%}".format(np.mean(predicao == labels)))





















