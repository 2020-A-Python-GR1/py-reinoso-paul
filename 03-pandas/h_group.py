# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 09:56:12 2020

@author: Paulr
"""

import pandas as pd
import numpy as np
import math

path_guardado="C://Users//Paulr//Documents//Git-Kraken//py-reinoso-paul//03-pandas//data//artwork_data.pickle"

df=pd.read_pickle(path_guardado)

seccion_df=df.iloc[49980:50019,:].copy()

df_agrupar_artista=seccion_df.groupby('artist')
print(type(df_agrupar_artista))

for columna,df_agrupado in df_agrupar_artista :
    print(type(columna))
    print(columna)
    print(type(df_agrupado))
    print(df_agrupado)

#calculos en colimnas del DF

a =seccion_df['units'].value_counts() # 38(mm)
                                      # 1 nan
#verificamos silas columnas estan vacias

print(seccion_df['units'].empty)
print(a.empty)

def llenar_valores_vacios(series, tipo):
    lista_valores = series.value_counts()
    # Si esta vacio no hacemos nada
    if(lista_valores.empty == True):
        return series
    else:
        if(tipo == 'promedio'):
            suma = 0
            numero_valores = 0
            for valor_serie in series:
                if(isinstance(valor_serie, str)): # veremos si es nan o no 
                    valor = int(valor_serie)      # valor a entero
                    numero_valores = numero_valores + 1 #sumanmos todos los valores para saber por cuanto dividir
                    suma = suma + valor                 # sumamos los valores de la columna
                else:
                    pass
            promedio = suma / numero_valores #calculamos el promedio
            series_valores_llenos = series.fillna(promedio) #llenamos la serie para los valores que no estan llenos el promedio
            return series_valores_llenos
        if(tipo == 'mas_repetido'):            
            valor_mas_repetido=series.value_counts().idxmax()  # obtenemos el val mas repetido
            series_valores_llenos = series.fillna(valor_mas_repetido) #llenamos la serie para los valores que no estan llenos el mas repetido
            return series_valores_llenos            
        
            

def transformar_df(df):
    df_artist = df.groupby('artist') #agrupamos los artistas
    lista_df = []
    for artista, df in df_artist:
        copia_df = df.copy() #para no modificar el orginal

        serie_w = copia_df['width'] #definiremos las series que queremos llenar
        serie_h = copia_df['height']
        serie_u = copia_df['units']
        serie_i = copia_df['title']
        
        copia_df.loc[:, 'width']  = llenar_valores_vacios(  #copiamos los registros pero solo la columna with
            serie_w,              #llenaremos con la serie with 
            'promedio')           # y pondremos el valor promedio 
        
        copia_df.loc[:, 'height']  = llenar_valores_vacios(
            serie_h, 
            'promedio')
        # llenaremos estos con los valores mas repetidos
        copia_df.loc[:, 'units']  = llenar_valores_vacios(
            serie_u, 
            'mas_repetido')
        
        copia_df.loc[:, 'title']  = llenar_valores_vacios(
            serie_i, 
            'mas_repetido')
        
        lista_df.append(copia_df)       # a la lista agregamos los data frames agrupados por artistas
    df_completo = pd.concat(lista_df)   # podremos los dataframes en uno solo
    return df_completo                  #davolvemos el dtaframe completo

df_lleno = transformar_df(seccion_df)



    





