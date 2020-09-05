# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

# ../../images/thumbnail/294930.jpg
# https://www.fybeca.com/images/thumbnail/294930.jpg

def transformar_url_imagen(texto):
    url_fybeca='https://www.fybeca.com'
    cadena_texto='../..'
    return texto.replace(cadena_texto,url_fybeca)


class ProductoFybeca(scrapy.Item):
    titulo=scrapy.Field()
    imagen=scrapy.Field(
        input_processor=MapCompose( #resive lista de fucniones
            transformar_url_imagen
        ),
        output_processor=TakeFirst() #obtenemos un alista[]
                                     #sacamos el primero de la lista
    )
















class ItemFybecaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
