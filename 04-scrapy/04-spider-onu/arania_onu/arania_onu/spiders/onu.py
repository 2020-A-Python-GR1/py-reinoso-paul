import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu (CrawlSpider):
    name='crawl_onu' #Heredado

    allowed_domais= [  #Heredado-dominios permitidos
        'un.org'
    ]

    start_urls= [  #urls donde vamos a empezar
        'https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html'
    ]

    regla_uno=(
        Rule(
            LinkExtractor(),
            callback='parse_page' #nombre d efuncion a ejecutar para parsear
        ),
        # segundo parametro vacio
    )

    segmentos_url_permitidos=(
        'funds-programmes-specialized-agencies-and-others'
    )

    regla_dos=(
        Rule(
            LinkExtractor(
                allow_domains=allowed_domais,
                allow=segmentos_url_permitidos
            ),callback='parse_page'
        ),
        #parametro vacio
    )

    segmentos_restringidos=(
        'ar/sections',
        'zh/sections',
        'ru/sections'
        )

    regla_tres=(
        Rule(
            LinkExtractor(
                allow_domains=allowed_domais,
                allow=segmentos_url_permitidos,
                deny=segmentos_restringidos
            ),callback='parse_page'
        ),
        #parametro vacio
    )



    rules = regla_tres #Heredado

    def parse_page(self,response):
        lista_programas= response.css('.field-item>h4::text').extract()
        #lista_programas= response.css(''div.field-items > div.field-item > h4::text'').extract()        
        for agencia in lista_programas:
            with open('onu_agencias.txt','a+',encoding='utf-8') as archivo:
                archivo.write(agencia+'\n')
