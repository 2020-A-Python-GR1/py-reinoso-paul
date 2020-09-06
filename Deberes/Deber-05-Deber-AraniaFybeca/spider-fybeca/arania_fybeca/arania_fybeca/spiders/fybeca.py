import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu (CrawlSpider):
    name='arania_craw_fybeca' #Heredado

    allowed_domais= [  #Heredado-dominios permitidos
        'fybeca.com'
    ]

    start_urls= [  #urls donde vamos a empezar

        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=446&s=0&pp=5000'
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=537&s=0&pp=5000',        
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=627&s=0&pp=5000',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=558&s=0&pp=5000',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=489&s=0&pp=5000',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=562&s=0&pp=5000'                
    ]

    segmentos_url_permitidos=(        
        'cat=446&s=0&pp=5000',
        'cat=537&s=0&pp=5000',
        'cat=627&s=0&pp=5000',
        'cat=558&s=0&pp=5000',
        'cat=489&s=0&pp=5000',
        'cat=562&s=0&pp=5000'                
    )

    segmentos_restringidos=(
        'pages/detail.jsf'
    )

    regla_tres=(
        Rule(
            LinkExtractor(
                allow_domains=allowed_domais,
                allow=segmentos_url_permitidos,
                deny=segmentos_restringidos
            ),callback='parse_page'  #nombre de funcion a ejecutar para parsear
        ),
        #parametro vacio
    )

    rules = regla_tres #Heredado

    def parse_page(self,response):
 
        etiqueta_contenedora=response.css(
            'li.product-tile'
        )


        nombre_producto=etiqueta_contenedora.css(
            'div.product-tile-inner>a.name::text'
        ).extract()

        #print(nombre_producto)
        
        # extraemos los precios de mienbros de  los productos
        precio_miembro_producto=etiqueta_contenedora.css(
            'div.price-member > div::attr(data-bind)'
        ).extract()

        #"text:'$' + (15.99).formatMoney(2, '.', ',')"
        precio_miembro_producto_formato=list()
        precio_miembro_producto_form=list()
        for i in precio_miembro_producto:
            precio_miembro_producto_formato.append(i.strip('text:\'$\' + (').strip(').formatMoney(2, \'.\', \',\')"'))
        
        for j in precio_miembro_producto_formato:                
            precio_miembro_producto_form.append(float(j))

        print('Minimo precio para Miebro',min(precio_miembro_producto_form))
        print('Maximo precio para Miebro',max(precio_miembro_producto_form))


        # extraemos los precios comunes de  los productos
        precio_producto=etiqueta_contenedora.css(
            'div.price::attr(data-bind)'
        ).extract()

        #"text:'$' + (4.87).formatMoney(2, '.', ',')"
        precio_producto_formato=list()
        precio_producto_form=list()
        for i in precio_producto:
            precio_producto_formato.append(i.strip('text:\'$\' + (').strip(').formatMoney(2, \'.\', \',\')"'))


        for j in precio_producto_formato:                
            precio_producto_form.append(float(j))

        print('Minimo precio comun',min(precio_producto_form))
        print('Maximo precio comun',max(precio_producto_form))
        z=0
        for n in precio_miembro_producto_form:
            z=z+n
        print('Total miembros',z)            
        k=0
        for m in precio_producto_form:
            k=k+m
        print('Total normal',k)    

        print("Ahorro de compra:",(z-k))    
              
        for precio in precio_producto_formato:
            with open('precios_comunes.txt','a+',encoding='utf-8') as archivo:
                archivo.write(precio+'\n')

        for precio in precio_miembro_producto_formato:
            with open('precios_miembros.txt','a+',encoding='utf-8') as archivo:
                archivo.write(precio+'\n')