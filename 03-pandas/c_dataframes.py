# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:47:25 2020

@author: Paulr
"""


import numpy as np
import pandas as pd

arr_pand=np.random.randint(0,10,6).reshape(2,3)

df1=pd.DataFrame(arr_pand)

s1=df1[0]
s2=df1[1]
s3=df1[2]

df1[3]=s1

df1[4]=s1*s2


datos_fisicos_uno=pd.DataFrame(
    arr_pand,
    columns=[
        'Estatura (cm)',
        'Peso (kg)',
        'Edad (anios)'
        ],
    index=[
        'Paul',
        'Martin'
        ]
    )

serie_peso=datos_fisicos_uno['Peso (kg)']
datos_paul=serie_peso['Paul']
print(serie_peso)
print(datos_paul)


df1.index=['Paul','Nicolas']
df1.index=['Esteban','Francisco']
df1.columns=['A','B','C','D','E']























