import scrapy

class IntroSpider(scrapy.Spider):
    name='introduccion_spider'

    urls=[ 
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    
    def parse(self,response):
        etiqueta_contenedora=response.css(
            'article.product_pod'
        )
        #extrae los titulos de los libros
        titulos=etiqueta_contenedora.css(
            'h3 >a::text'
        ).extract()

        #Obtener imagen dinero y stock (opcional estrellas)#

        urls_imagenes=etiqueta_contenedora.css( # capturo con el atributo src
            'div.image_container>a>img::attr(src)'
        ).extract()

        precios=etiqueta_contenedora.css( # capturo los precios 
            'p.price_color::text'
        ).extract()

        en_stocks=etiqueta_contenedora.css( # capturo el texto de stock
            'p.instock::text'
        ).extract()

        num_estrellas=etiqueta_contenedora.css( # las estrellas de los libros
            'p.star-rating::attr(class)'
        ).extract()

        print("*****Titulos de libros*****")
        print(titulos)
        print("*****URLS de libros*****")
        print(urls_imagenes)
        print("*****Precios de libros*****")
        print(precios)
        print("*****stokcs de libros*****")
        print(en_stocks)
        print("*****estrellas de libros*****")
        print(num_estrellas)
        
        #trabajamos con listas de strings

        #eliminamos el caracter especial y transformamos a float precio

        precio_con_formato=list()
        for i in precios:                        
            precio_i = list(i)
            precio_con_formato.append(float(''.join(precio_i[1:])))
        #print(precio_con_formato)
        #print(type(precio_con_formato[0]))
        
        #eliminamos saltos y espacios en blanco para el stock

        stock_con_formato=list()
        for i in en_stocks:
            stock_con_formato.append(i.strip(' ').strip('\n    \n'))

        for i in stock_con_formato:
            stock_con_formato.remove("")                        
        #print(stock_con_formato)
        #print(type(stock_con_formato[0]))

        #eliminamos saltos y espacios en blanco para el stock
        
        estrellas_formato=list()
        for i in num_estrellas:            
            estrellas_formato.append(i.strip('').strip('star-rating '))
        #print(estrellas_formato)
        #print(type(estrellas_formato[0]))        
        
        print("*****Titulos de libros*****")
        print(titulos)
        print("*****URLS de libros*****")
        print(urls_imagenes)
        print("*****Precios de libros*****")
        print(precio_con_formato)
        print("*****stokcs de libros*****")
        print(stock_con_formato)
        print("*****estrellas de libros*****")
        print(estrellas_formato)




