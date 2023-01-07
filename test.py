from my_graph import tSNE_on_image
import numpy as np

from sklearn.datasets import fetch_olivetti_faces

X=fetch_olivetti_faces()["data"]
y=fetch_olivetti_faces()["target"]

#X["data"]=[X["data"][i].reshape(64,64) for i in range(len(X))]
temp=[]
for i in range(len(X)):
    temp.append(X[i].reshape(64,64))
    
Z=tSNE_on_image(temp,y)

