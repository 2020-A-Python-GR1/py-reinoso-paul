# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:33:03 2020

@author: Paulr
"""

import pandas as pd

path_guardado="C://Users//Paulr//Documents//Git-Kraken//py-reinoso-paul//03-pandas//data//artwork_data.pickle"


df=pd.read_pickle(path_guardado)

#artistas diplucados

serie_artistas_duplicados=df['artist']


#artistas sin que repitan
artistas=pd.unique(serie_artistas_duplicados)

print(type(artistas)) #numpy array
print(artistas.size)
print(len(artistas))

#obras de cierto artista

blake=df['artist']=='Blake, William' #serie

print(blake.value_counts())

df_fitrado_blake=df[blake]




















