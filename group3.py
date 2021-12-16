#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:10:51 2021

@author: celia
"""

import pandas as pd

df = pd.read_csv(r'liste_apprenants.csv', encoding="utf-8", sep=",")

final_data = df.drop(labels=[0,1,2,3], axis=0)
final_data=final_data[['Prénom']]

# Shuffle data 
shuffle= final_data.sample(frac=1).reset_index(drop=True)

# Taille du groupe
SIZE = 4 

# Creation d'un numéro de groupe
shuffle['group'] = shuffle.index // SIZE

#Liste des groupes
groups = [shuffle[shuffle['group']== num]      
    for num in range(shuffle['group'].max() + 1)]

print(groups[0],'__________________\n \n',groups[1],'__________________\n \n',groups[2],'__________________\n \n',groups[3])


