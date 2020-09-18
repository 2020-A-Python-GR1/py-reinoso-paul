import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import pandas as pd


class SerieSpider(CrawlSpider):
    name = 'arania_juego_csv'

    start_urls = [
        'https://www.nintenderos.com/juegos/'
    ]

    for i in range(1, 20):
        start_urls.append(
            'https://www.nintenderos.com/juegos/page/{i}/'.format(i=i))

    segmentos_url_permitidos = (
        'juego'
    )

    allowed_domains = [
        'nintenderos.com'
    ]

    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                allow=segmentos_url_permitidos
            ),
            callback='parse'
        ),
    )

    regla_uno = (
        Rule(
            LinkExtractor(),
            callback='parse_page'  # nombre funcion a ejecutar para parsear
        ),
        # segundo parametro vacio
    )

    rules = regla_uno
    name_serie = []

    def parse_page(self, response):

        # response.css('h1.c-post-single__title ::text').extract() obtienen nombre del juego
        # response.css('div.top ::text').extract() obtienen puntaje del juego
            
        name_serie = response.css(
            'div.c-post-single__container > ul.caracteristicas ::text').extract()[2]
        self.name_serie.append(name_serie)
        #info_uno=response.css('div.col-md-6 > ul.li-inl ::text').extract()
        #info_dos=response.css('div.mod-li > ul.li-inl ::text').extract()
        # print(info_dos)
        # print(info_uno)
        # for nb in nombre:
        #    with open('nombres_juegos.txt','a+',encoding='utf-8') as archivo:
        #        archivo.write(nb+'\n')

    def closed(self, reason):
        save_path = '../series.csv'
        df = pd.DataFrame({
            'name_serie': pd.Series(self.name_serie),
            #'release_date': pd.Series(self.release_date),
            #'runtime': pd.Series(self.runtime),
            #'end_date': pd.Series(self.end_date),
            #'genre': pd.Series(self.genre),
            #'rating': pd.Series(self.rating),
            #'votes': pd.Series(self.rating_votes)
        }
        )
        df.to_csv(save_path, index=False)
