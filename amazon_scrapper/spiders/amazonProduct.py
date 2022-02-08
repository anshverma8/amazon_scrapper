from numpy import product
import scrapy
from amazon_scrapper.items import AmazonScrapperItem

queries = ['samsung', 'motorola']


class AmazonproductSpider(scrapy.Spider):
    name = 'amazonProduct'
    allowed_domains = ['amazon.in']
    initialUrl = 'https://www.amazon.in/s?k='
    start_urls = [] 

    for query in queries:
        start_urls.append(initialUrl + query)
    
    def parse(self, response):
        items = AmazonScrapperItem()
        items['productName'] = response.css('.s-line-clamp-2::text').extract()
        items['productPrice'] = response.css('.a-price-whole::text').extract()
        yield items