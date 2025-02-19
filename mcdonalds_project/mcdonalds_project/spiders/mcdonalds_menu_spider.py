import scrapy
from mcdonalds_project.items import McdonaldsMenuItem

class McdonaldsMenuSpider(scrapy.Spider):
    """Get menu products from mcdonalds"""
    name = 'mcd_m'
    start_urls = ['https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html']
    custom_settings = {
        'FEEDS': {
            'mcdonalds_menu_urls.json': {
                'format': 'json',
                'encoding': 'utf8',
                'indent': 4,
                'overwrite': True
            }
        }
    }

    def parse(self, response):
        # Получаем все элементы списка товаров
        products = response.css('li.cmp-category__item')
        
        # Выводим все найденные ссылки и имена
        for product in products:
            item = McdonaldsMenuItem()
            item['url'] = response.urljoin(product.css('a.cmp-category__item-link::attr(href)').get())
            item['id'] = product.css('::attr(data-product-id)').get()
            item['name'] = product.css('div.cmp-category__item-name::text').get().strip()
            yield item