# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 07:57:52 2020

@author: Paulr
"""

import numpy as np
import pandas as pd

lista_numero=[1,2,3,]
tupla_numero=(1,2,3)
np_numeros=np.array((1,2,3,4))


series_a=pd.Series(
    lista_numero
    )

series_b=pd.Series(
    tupla_numero
    )

series_c=pd.Series(
    np_numeros
    
    )


series_d=pd.Series(
    [True,
    False,
    12,
    12.12,
    "Paul",
    None,
    (1),
    [2],
    {"nombre":"Paul"}]
    )

print(series_d[3])

lista_ciudades=[
    "Ambato",
    "Cuenca",
    "Loja",
    "Quito"
    ]

serie_ciudad=pd.Series(
    lista_ciudades,
    index=[
        "A",
        "C",
        "L",
        "Q"]    
    )

print (serie_ciudad[3])
print (serie_ciudad["C"])



valores_cuidad={
    "Ibarra":9500,
    "Guayaquil":100000,
    "Cuenca":7000,
    "Quito":8000,
    "Loja":3000
    }

series_valor_ciudad=pd.Series(
    valores_cuidad
    )

#filtrado de ciudades<1000

ciudades_menos_5k=series_valor_ciudad<5000
print(type(series_valor_ciudad))
print(type(ciudades_menos_5k))
print(ciudades_menos_5k)


s5 = series_valor_ciudad[ciudades_menos_5k]
print(s5)
series_valor_ciudad=series_valor_ciudad*1.1


series_valor_ciudad["Quito"]=series_valor_ciudad["Quito"]-50





































