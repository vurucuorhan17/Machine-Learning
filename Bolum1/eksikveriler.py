# -*- coding: utf-8 -*-
"""
Created on Mon May  7 00:43:04 2018

@author: orhan
"""

#kutuphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#kodlar
#veri yukleme

veriler = pd.read_csv("eksikveriler.csv")

print(veriler)

#eksik veriler
#sci-kit learn

from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values="NaN",strategy="mean",axis=0)

Yas = veriler.iloc[:,1:4].values

print(Yas)

imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)

