# -*- coding: utf-8 -*-
"""
Created on Mon May  7 00:43:04 2018

@author: orhan
"""

#kutuphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,Imputer


#kodlar
#veri yukleme

veriler = pd.read_csv("eksikveriler.csv")

print(veriler)

#eksik veriler
#sci-kit learn

imputer = Imputer(missing_values="NaN",strategy="mean",axis=0)

Yas = veriler.iloc[:,1:4].values

print(Yas)

imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)




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

sonuc = pd.DataFrame(data = ulke,index = range(22),columns=['fr','tr','us'])
print(sonuc)

sonuc2 = pd.DataFrame(data = Yas,index = range(22),columns=['boy','kilo','yas'])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values
#print(cinsiyet)

sonuc3 = pd.DataFrame(data = cinsiyet,index = range(22),columns=['cinsiyet'])
print(sonuc3) 

s = pd.concat([sonuc,sonuc2],axis=1) #pd.concat Data Frame'leri birleştirir.
print(s)

s2 = pd.concat([s,sonuc3],axis=1)
print(s2)