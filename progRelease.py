#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:01:19 2021

@author: victorien
"""

import pandas as pd
from random import sample
import random
import numpy

# Group 4
def Tirage5():
    df = pd.read_csv('liste_apprenants.csv')
    
    #etudiants = df.iloc[4:20,0]
    etudiants = df.iloc[:, 0]
    
    def selectRandom(names):
        return numpy.random.choice(names,1)
    
    # On melange notre dataframe
    L = etudiants.tolist()
    random.shuffle(L)
    
    
    liste1 = []
    liste2 = []
    liste3 = []
    
    cpt = 1
    
    for i in L:
        if cpt <= 5:
            liste1.append(i)
        elif cpt > 5 and cpt <= 10:
            liste2.append(i)
        else:
            liste3.append(i)
    
        cpt = cpt + 1
        
    print('liste1',liste1)
    print('liste2',liste2)
    print('liste3',liste3)
    
    new_df = pd.DataFrame({'Colonne 1':[liste1[0], liste2[0], liste3[0]],
                           'Colonne 2':[liste1[1], liste2[1], liste3[1]],
                           'Colonne 3':[liste1[2], liste2[2], liste3[2]],
                           'Colonne 4':[liste1[3], liste2[3], liste3[3]],
                           'Colonne 5':[liste1[4], liste2[4], liste3[4]],
                           'Colonne 6':[liste3[5], None, None]})
    
    return new_df

# Programme principal
df = Tirage5()
print(df)





