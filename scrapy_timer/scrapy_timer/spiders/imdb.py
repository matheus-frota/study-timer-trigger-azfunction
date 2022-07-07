import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=adventure&sort=user_rating,desc']
    
    def parse(self, response):

        titles = response.css('div .lister-item-content h3 a::text').getall()
        data_lancamentos = response.css('div .lister-item-content h3 span.lister-item-year::text').re('\((\d.*)\)')
        duracoes = response.css('div .lister-item-content p.text-muted span.runtime::text').getall()
        generos = response.css('div .lister-item-content p.text-muted span.genre::text').getall()
        ratings = response.css('div .lister-item-content div.ratings-imdb-rating strong::text').getall()
        metascores = response.css('div .lister-item-content div.ratings-metascore span::text').getall()
        next_page = response.css('div.desc a lister-page-next::attr(href)').getall()

        

