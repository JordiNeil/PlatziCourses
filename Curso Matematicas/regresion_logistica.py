# -*- coding:utf-8 -*-
import numpy as np 
from sklearn.linear_model import LogisticRegression
x = np.array([0.5, 0.75, 1, 1.25, 1.5, 1.75, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 4, 4.25, 4.5,
4.75, 5, 5.5]).reshape(-1,1)
y = ([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])

regresion_logictica = LogisticRegression()

regresion_logictica.fit(x,y)

x_nuevo = np.array([1,2,3,4,5,6]).reshape(-1,1)

prediccion = regresion_logictica.predict(x_nuevo)
print(prediccion)

probabilidades_prediccion = regresion_logictica.predict_proba(x_nuevo)
print(probabilidades_prediccion)
print(probabilidades_prediccion[:,1])