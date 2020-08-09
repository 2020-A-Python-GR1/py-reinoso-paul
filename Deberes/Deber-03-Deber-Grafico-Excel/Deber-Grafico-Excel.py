# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 15:25:22 2020

@author: Paulr
"""

import numpy as np
import pandas as pd
import os
import xlsxwriter

path_guardado="C://Users//Paulr//Documents//Git-Kraken//py-reinoso-paul//03-pandas//data//artwork_data.pickle"

df = pd.read_pickle(path_guardado)
sub_df=df.iloc[49980:50519,:].copy()

path_excel_colores_grafica ="C://Users//Paulr//Documents//Git-Kraken//py-reinoso-paul//Deberes//Deber-03-Deber-Grafico-Excel//artwork_data_colores_gafica.xlsx"
# artwork_data_colores.xlsx
writer = pd.ExcelWriter(path_excel_colores_grafica, engine='xlsxwriter')
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

############## Grafica  ###############

#leer del excel
data_colores=pd.ExcelFile(path_excel_colores_grafica)
data_uno=data_colores.parse('Artistas')


workbook = xlsxwriter.Workbook("C://Users//Paulr//Documents//Git-Kraken//py-reinoso-paul//Deberes//Deber-03-Deber-Grafico-Excel//Grafico_Excel.xlsx")

worksheet = workbook.add_worksheet()

worksheet.add_table('A1:B85',
                    {'data': data_uno.values.tolist(),
                     'style': 'Table Style Light 9',
                     'columns': [{'header': 'Artistas'},
                                        {'header': 'Cantidad Art'}]}
                    )

chart = workbook.add_chart({'type': 'column'})


chart.set_plotarea({
    'gradient': {'colors': ['#FFEFD1', '#F0EBD5', '#B69F66']}
})

chart.add_series({
    'name':       '=Sheet1!$A$1',
    'categories': '=Sheet1!$A$2:$A$85',
    'values':     '=Sheet1!$B$2:$B$85',
})

worksheet.insert_chart('D2', chart)

workbook.close()















