import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import pandas as pd


class SerieSpider(CrawlSpider):
    name = 'arania_juego_csv'

    start_urls = [
        'https://www.nintenderos.com/juegos/'
    ]

    for i in range(1, 29):
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
    desarrolladores=list()
    distribuidor=list()
    editor=list()
    generos=list()
    plataforma=list()
    precio_lanzamiento=list()
    consola_virtual=list()
    lanzamiento_europa=list()
    formato =list()
    voces_texto=list()
    textos_idioma=list()
    jugadores=list()
    modo_online=list()
    num_idiomas=list()
    num_generos=list()
    nombre=list()
    puntos=list()
    edad_rec=list()

    def parse_page(self, response):

        # consultas
        nombre_juego=response.css('h1.c-post-single__title ::text').extract()[0] #obtienen nombre del juego
        puntuacion_juego=response.css('div.top ::text').extract()[3]# obtienen puntaje del juego
        edad_recomendada=response.css('div.pegi-image img::attr(alt)').extract()[0] #edad recomendada            
        name_serie = response.css('div.c-post-single__container > ul.caracteristicas ::text').extract() #toda la informacion general
        #limpiamos        
        completo=list()
        for i in name_serie:
            completo.append(i.strip("\n\t\t\t\t\t\t").strip("\n\t\t").strip("\t\t\t\t\t\t").strip(",").strip(" ").strip("\n"))        
        completo = list(filter(None, completo))
        
        #Formato para generos/unimos los generos en un solo campo
        generos=list()        
        indices_genero=list()
        cont=0
        for i in range((completo.index("Géneros:")+1),len(completo)):
            if(i<completo.index("Plataforma:")):
                generos.append(completo[i])
                cont=cont+1
                indices_genero.append(i)
        
        for x in range(0,len(indices_genero)):
            completo.pop(indices_genero[x])

        gener='-'.join(generos)        
        completo.insert((completo.index("Géneros:")+1),gener)
        print("GENEROS",cont)
                        
        #formato para el texto de idioma
        for i in range((completo.index("Textos (idioma):")+1),len(completo)):
            if(i<completo.index("Jugadores:")):
                num_idiomas = len(completo[i].split(','))
                idiom=completo[i].replace(', ', '-')                
                completo.pop(i)                
        print("IDIOMAS",num_idiomas)        
        completo.insert((completo.index("Textos (idioma):")+1),idiom)        
                
        self.nombre.append(nombre_juego)        
        self.puntos.append(puntuacion_juego)
        self.edad_rec.append(edad_recomendada)
        self.desarrolladores.append(completo[(completo.index('Desarrollador:')+1)])        
        self.generos.append(completo[(completo.index('Géneros:')+1)])
        self.plataforma.append(completo[(completo.index('Plataforma:')+1)])
        self.precio_lanzamiento.append(completo[(completo.index('Precio de lanzamiento:')+1)])
        self.consola_virtual.append(completo[(completo.index('Consola virtual:')+1)])
        self.lanzamiento_europa.append(completo[(completo.index('Lanzamiento en Europa:')+1)])
        self.formato.append(completo[(completo.index('Formato:')+1)])
        self.voces_texto.append(completo[(completo.index('Voces (idioma):')+1)])
        self.textos_idioma.append(completo[(completo.index('Textos (idioma):')+1)])
        self.jugadores.append(completo[(completo.index('Jugadores:')+1)])
        self.modo_online.append(completo[(completo.index('Modo Online:')+1)])        
        self.distribuidor.append(completo[(completo.index('Distribuidor:')+1)])
        self.num_generos.append(cont)
        self.num_idiomas.append(num_idiomas)

    def closed(self, reason):
        save_path = '../series.csv'
        df = pd.DataFrame({
            
            'Nomre': pd.Series(self.nombre),
            'Puntuacion': pd.Series(self.puntos),
            'Clasificacion Edad': pd.Series(self.edad_rec),
            'Desarrollador': pd.Series(self.desarrolladores),
            'Distribuidor': pd.Series(self.distribuidor),
            'Géneros': pd.Series(self.generos),
            'Plataforma': pd.Series(self.plataforma),
            'Precio': pd.Series(self.precio_lanzamiento),
            'Consola virtual': pd.Series(self.consola_virtual),
            'Lanzamiento en Europa:': pd.Series(self.lanzamiento_europa),
            'Formato': pd.Series(self.formato),
            'Voces (idioma)': pd.Series(self.voces_texto),
            'Textos (idioma)': pd.Series(self.textos_idioma),
            'Num Jugadores': pd.Series(self.jugadores),
            'Modo Online': pd.Series(self.modo_online),
            'Num genero': pd.Series(self.num_generos),
            'Num idioma': pd.Series(self.num_idiomas),
        }
        )
        df.to_csv(save_path, index=False)
