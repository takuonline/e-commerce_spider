# -*- coding: utf-8 -*-
import scrapy

class ECommerceSpider(scrapy.Spider):
    name = 'e-commerce'

    def start_requests(self):
        url = 'https://www.shoprite.co.za/c-2256/All-Departments/'
        yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        # products
        # //div[@class='product__listing product__grid']

        # image link
        # .//div[@class='item-product__image']/a/img/@data-original-src


        # title
        # .//h3[@class='item-product__name']/a/text()

        # price
        # .//div[@class='special-price__price']/span/text()[1]

        # promotion valid date
        # .//span[@class='item-product__valid']/text()

        # promotion
        # .//span[@class='item-product__message__text']/text()

        # pagination link
        # .//a[@class='shoprite-icon-chevron-right']/@href


        # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        
        for item in response.xpath("//div[@class='item-product']"):
            yield{
                "title": item.xpath(".//h3[@class='item-product__name']/a/text()").extract_first(),
                "price": item.xpath(".//div[@class='special-price__price']/span/text()[1]").extract_first() + item.xpath(".//div[@class='special-price__price']/span/sup/text()").extract_first() ,
                "image_url": "https://www.shoprite.co.za" + item.xpath(".//div[@class='item-product__image']/a/img/@data-original-src").extract_first(),
                # "promotion_valid_date": item.xpath(".//span[@class='item-product__valid']/text()").extract_first(),
                # "promotion": item.xpath("/html/body/main/div[4]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/figure/figcaption/div[1]/span[2]/a/span/text()").extract_first()
            }
        # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        # print(self.arg)

        next_page = response.xpath("/html/body/main/div[4]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/ul/li[8]/a/@href").extract_first()

        if (next_page is not None):
            next_page_link = f"https://www.shoprite.co.za{next_page}"
            yield scrapy.Request(url=next_page_link, callback=self.parse)

