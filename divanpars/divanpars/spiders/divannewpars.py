import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://divan.ru/category/divany-i-kresla"]
    # start_urls = ["https://www.divan.ru/category/svet"]

    def parse1(self, response):
        divans = response.css('div._Ud0k')
        for divan in divans:
            yield {
                'name': divan.css('div.lsooF span::text').get(),
                'price': divan.css('div.pY3d2 span::text').get(),
                'url': divan.css('a').attrib['href']
            }

    def parse(self, response):
        lamps = response.css('div._Ud0k')
        for lamp in lamps:
            yield {
                'name': lamp.css('div.lsooF span::text').get(),
                'price': lamp.css('div.pY3d2 span::text').get(),
                'url': lamp.css('a').attrib['href']
            }
