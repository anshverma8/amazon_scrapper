from numpy import product
import scrapy
from amazon_scrapper.items import AmazonScrapperItem

queries = ['samsung', 'motorola']


class AmazonproductSpider(scrapy.Spider):
    name = 'amazonProduct'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/s?k=' + queries[0],
    'https://www.amazon.in/s?k=' + queries[1]] 

    def parse(self, response):
        items = AmazonScrapperItem()
        items['productName'] = response.css('.s-line-clamp-2::text').extract()
        items['productPrice'] = response.css('.a-price-whole::text').extract()
        yield items