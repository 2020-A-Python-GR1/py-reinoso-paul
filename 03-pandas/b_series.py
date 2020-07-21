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


svc_cuadrado=np.square(series_valor_ciudad)


ciudades_uno=pd.Series({
    "Montañita":300,
    "Guayaqui":10000,
    "Quito":2000,
    })

ciudades_dos=pd.Series({
    "Loja":300,
    "Guayaqui":10000    
    })

ciudades_uno["Loja"]=0


print(ciudades_uno+ciudades_dos)

ciudades_add=ciudades_uno.add(ciudades_dos)


ciud_concat=pd.concat([
    ciudades_uno,
    ciudades_dos    
    ])


#ciud_concat_verify=pd.concat([
#    ciudades_uno,
#    ciudades_dos    
#    ], verify_integrity=True)



#ciud_concat_verifyA=ciudades_uno.append(
#    ciudades_dos,
#    verify_integrity=False)


print(ciudades_uno.max())
print(pd.Series.max(ciudades_uno))
print(np.max(ciudades_uno))


print(ciudades_uno.min())
print(pd.Series.min(ciudades_uno))
print(np.min(ciudades_uno))


print(ciudades_uno.mean())
print(ciudades_uno.median())
print(np.average(ciudades_uno))

print(ciudades_uno.head(2))
print(ciudades_uno.tail(2))



print(ciudades_uno.sort_values(ascending=False).head(2))
print(ciudades_uno.sort_values().tail(2))

#0-1000 %5
#1001-5000 10%
#5001-20000 15%


def calcular(valor_serie):
    if(valor_serie<=1000):
        return valor_serie*1.05
    if(valor_serie > 1000 and valor_serie <= 5000):
        return valor_serie*1.10
    if(valor_serie>5000):
        return valor_serie*1.15

ciudad_calculada=ciudades_uno.map(calcular)



# if else
# Cuando NO cuemple la condicion, se aplica 

resultado=ciudades_uno.where(ciudades_uno<1000,
                             ciudades_uno*1.05)

series_numeros=pd.Series(['1.0','2',-3])

print(pd.to_numeric(series_numeros))

# 'interger, ''float' , 'unsigned','Float'

print(pd.to_numeric(series_numeros,downcast='integer'))


series_numeros_err=pd.Series(['no tiene','1.0','2',3])


# ignore, coerce, raise (default)
#print(pd.to_numeric(series_numeros_err))
print(pd.to_numeric(series_numeros_err, errors='ignore'))
print(pd.to_numeric(series_numeros_err, errors='coerce'))






































