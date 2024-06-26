import scrapy

class QuotesToScrapeSpider(scrapy.Spider):
    # Identidade
    name = 'frasebot'
    
    # Request
    def start_requests(self):
        urls = ['https://quotes.toscrape.com/']
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    # Response
    def parse(self, response):
        # Aqui você processa o que é retornado da response
        with open('pagina.html', 'wb') as arquivo:
            arquivo.write(response.body)
