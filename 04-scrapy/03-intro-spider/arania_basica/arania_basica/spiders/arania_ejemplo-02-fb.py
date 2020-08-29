import scrapy

class IntroSpider(scrapy.Spider):
    name='introduccion_spider_fybeca'

    urls=[ 
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=639&s=0&pp=25'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    
    def parse(self,response):
        etiqueta_contenedora=response.css(
            'li.product-tile'
        )
        # 1)necesitamos consultar: el nombre del producto, los dos precios y la imagen 
    
        # despues de obtener la informacion encontrar:

        # 1)obtener cual es el item con mayor y menor precio
        
        # 2)obtener cuanto ahorramos si compramos todos los productos como afiliado

        # extrae los nombres de los productos
        nombre_producto=etiqueta_contenedora.css(
            'div.product-tile-inner>a.name::text'
        ).extract()

        print(nombre_producto)

        
        # extraemos los precios de mienbros de  los productos
        precio_miembro_producto=etiqueta_contenedora.css(
            'div.price-member > div::attr(data-bind)'
        ).extract()

        print(precio_miembro_producto)


        # extraemos los precios comunes de  los productos
        precio_producto=etiqueta_contenedora.css(
            'div.price::attr(data-bind)'
        ).extract()

        print(precio_producto)

        # extraemos las imagenes de  los productos
        img_producto=etiqueta_contenedora.css(
            'a.image> img::attr(src)'
        ).extract()

        print(img_producto)

        # Darle formato a los datos y contestar las dos preguntas.


