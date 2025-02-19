# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class McdonaldsMenuItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    pass

class McdonaldsProductInfoItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    calories = scrapy.Field()
    fats = scrapy.Field()
    carbs = scrapy.Field()
    proteins = scrapy.Field()
    unsaturated_fats = scrapy.Field()
    sugars = scrapy.Field()
    salt = scrapy.Field()
    portion = scrapy.Field()
    pass