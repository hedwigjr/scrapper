import scrapy

class BookSpider(scrapy.Spider):
  name = 'spider'
  start_urls = ['https://habr.com/ru/search/?q=parse&target_type=posts&order=relevance']

#   def parse(self, response):
#       for link in response.css('a.tm-article-snippet__title-link::attr(href)'):
#         yield response.follow(link, callback=self.parse_page)
  def parse(self, response):
    for i in range(0,10):
        yield response.follow(response.css('a.tm-article-snippet__title-link::attr(href)')[i], callback=self.parse_page)
       
  def parse_page(self, response):
    author = response.css('a.tm-user-info__username::text').get()
    author = author.replace('\n    ','').strip()

    yield{
          'author': author ,
          'title': response.css('h1.tm-article-snippet__title_h1 span::text').get(),
          'url': response.request.url 
          
            }
