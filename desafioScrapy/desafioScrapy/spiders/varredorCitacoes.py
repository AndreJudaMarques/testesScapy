from typing import Any, Iterable
import scrapy
from scrapy.http import Response

#CamelCase
class VarredorCitacoes(scrapy.Spider):
      #identidade
      name= 'citacoesBot'
      #request
      def start_requests(self):
            #definir url(s) a varrer:
            urls = [' https://www.goodreads.com/quotes']

            for url in urls:
                  yield scrapy.Request(url=url, callback=self.parse)
      
      #Response
      def parse(self, response):
            #aqui onde deve processar o que é retornado da response
            for elemento in response.xpath("//div[@class='quoteText']"):
                  yield{
                        'frase' : elemento.xpath(".//div[@class='quoteText']/text()[1]").get(),
                        'autor' : elemento.xpath(".//span[@class='authorOrTitle']/text()").get(), 
                        'tags' : elemento.xpath(".//div[@class='greyText smallText left']").getall()
                  }
            