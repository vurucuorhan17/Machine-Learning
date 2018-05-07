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

veriler = pd.read_csv("veriler.csv")

print(veriler)
#veri on isleme

boy = veriler[['boy']]

print(boy)

boykilo = veriler[['boy','kilo']]

print(boykilo)

sayi = 25

class insan:
    boy = 180
    def kosmak(self,b):
        return b + 10
    
ali = insan()
print(ali.boy)
print(ali.kosmak(90))
