# Created by Vinicius Bertuol.

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer 
from sklearn import tree
import os

# Read dataset into data frame
df = pd.read_csv("info.csv")

# Predict using our model
rodada = 12
pnr = 10
vitorias = 4
empates = 4
derrotas = 4
gm = 21
gc = 16
sg = gm - gc
pontos = (vitorias * 3) + empates
aproveitamento = (pontos * 100) / (rodada * 3)

posiçoes = []

for i in range(1, 21):
    df["position"] = (df["pf"] <= i).astype(int)

    classes = ["No", "Yes"]
    y = df["position"].values

    columns = ["rodada","gm","gc","sg","pnr", "%",]
    features = df[list(columns)].values

    # Replace 'nans' by mean to avoid issues
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    X = imp.fit_transform(features)

    # Learn the decision tree
    clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=10)
    clf = clf.fit(X, y)

    if(clf.predict([[rodada,gm,gc,sg,pnr,aproveitamento]])):
            posiçoes.append(i)
            break

for i in range(20, 0, -1):
    df["position"] = (df["pf"] <= i).astype(int)

    classes = ["No", "Yes"]
    y = df["position"].values

    columns = ["rodada","gm","gc","sg","pnr", "%"]
    features = df[list(columns)].values

    # Replace 'nans' by mean to avoid issues
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    X = imp.fit_transform(features)

    # Learn the decision tree
    clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=10)
    clf = clf.fit(X, y)

    if not(clf.predict([[rodada,gm,gc,sg,pnr,aproveitamento]])):
        i = i+1
        posiçoes.append(i)
        break
    
os.environ["PATH"] += os.pathsep + r'C:\ProgramData\anaconda3\Library\bin\dot'

print(posiçoes)
        




