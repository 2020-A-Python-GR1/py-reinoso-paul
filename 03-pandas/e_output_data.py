# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:29:31 2020

@author: Paulr
"""
import numpy as np
import pandas as pd
import sqlite3
import os


path_guardado="C://Users//Paulr//Documents//Git-Kraken//py-reinoso-paul//03-pandas//data//artwork_data.pickle"



df = pd.read_pickle(path_guardado)

sub_df=df.iloc[49980:50519,:].copy()

# Tipos De Archivos

#Excel

path_excel ="C://Users//Paulr//Documents//Git-Kraken//py-reinoso-paul//03-pandas//data//artwork_data.xls"


#con indice como columna
sub_df.to_excel(path_excel)

#sin indice como columna
sub_df.to_excel(path_excel,index=False)

#selecion de columnas
columnas=['artist','title','year']
sub_df.to_excel(path_excel,columns=columnas)

# Multiples hojas de trabajo
path_excel_mt ="C://Users//Paulr//Documents//Git-Kraken//py-reinoso-paul//03-pandas//data//artwork_data_mt.xls"

writer=pd.ExcelWriter(path_excel_mt, engine='xlsxwriter')

sub_df.to_excel(writer,sheet_name='Primera')
sub_df.to_excel(writer,sheet_name='Segunda')
sub_df.to_excel(writer,sheet_name='Tercera')

writer.save()

# Formato Condicional #
path_excel_colores ="C://Users//Paulr//Documents//Git-Kraken//py-reinoso-paul//03-pandas//data//artwork_data_colores.xls"
# artwork_data_colores.xlsx

writer = pd.ExcelWriter(path_excel_colores, engine='xlsxwriter')
# Series

num_artistas = sub_df['artist'].value_counts()

print(type(num_artistas))
print(num_artistas)

num_artistas.to_excel(writer, sheet_name = 'Artistas')

# Seleccionando la hoja de trabajo #

hoja_artistas = writer.sheets['Artistas']

# Formato #

ultimo_numero = len(num_artistas.index) + 1

# rango_celdas = 'B2:B{}'.format()

rango_celdas = f'B2:B{ultimo_numero}'

print(rango_celdas)

formato_artistas = {
        "type": "2_color_scale",
        "min_value": "10",
        "min_type": "percentile",
        "max_value": "99",
        "max_type": "percentile"}

hoja_artistas.conditional_format(rango_celdas, formato_artistas)
writer.save()

########## SQL ##########

with sqlite3.connect("bdd_artist.bdd") as conexion:
    sub_df.to_sql('py_artistas', conexion)
    

## with mysql.connect('mysql://user:password@ip:puerto/nombre_base')
##      df5.to_sql('tabla_mysql', conexion)
    
########## JSON ##########

sub_df.to_json('artistas.json')

sub_df.to_json('artistas_tabla.json', orient = 'table')



