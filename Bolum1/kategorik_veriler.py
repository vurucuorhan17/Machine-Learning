# -*- coding: utf-8 -*-
"""
Created on Mon May  7 00:43:04 2018

@author: orhan
"""

#kutuphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

#kodlar
#veri yukleme

veriler = pd.read_csv("veriler.csv")

print(veriler)

#veriler'den ülke kolonunuu aldık
ulke = veriler.iloc[:,0:1].values
print(ulke)

#kategorik verileri numerik verilere dönüştürdük
le = LabelEncoder()

ulke[:,0] = le.fit_transform(ulke[:,0])
print(ulke)

#dönüşen verileri kolonun tepesine yerleştirdik ve bu sayede tr,us,fr'ye göre olan durumları
#ölçebiliriz

ohe = OneHotEncoder(categorical_features="all")
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)