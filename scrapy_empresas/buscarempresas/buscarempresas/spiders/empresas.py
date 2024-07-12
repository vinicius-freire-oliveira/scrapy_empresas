import scrapy


class MveSpider(scrapy.Spider):
    name = "empresas"
    #allowed_domains = ["forbes.com.br"]
    start_urls = ["https://forbes.com.br/forbes-money/2023/01/as-10-marcas-mais-valiosas-do-mundo-em-2023/"]

    def parse(self, response):
        for empresa in response.css('h2~ p'):
            empresa = empresa.css('strong::text').get()            
            yield {
                'Top 10 das marcas mais valiosas do mundo (em US$ bilhões):':empresa
            }
