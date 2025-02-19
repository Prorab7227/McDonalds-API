import scrapy
from mcdonalds_project.items import McdonaldsProductInfoItem
import json

class McdonaldsProductInfoSpider(scrapy.Spider):
    """Get product full info from mcdonalds"""
    name = 'mcd_i'
    
    def start_requests(self):
        with open('mcdonalds_menu_urls.json', 'r', encoding='utf-8') as f:
            items = json.load(f)
            for item in items:
                url = f"https://www.mcdonalds.com/dnaapp/itemDetails?country=UA&language=uk&showLiveData=true&item={item['id']}"
                yield scrapy.Request(url=url, callback=self.parse)
    
    custom_settings = {
        'FEEDS': {
            'mcdonalds_products.json': {
                'format': 'json',
                'encoding': 'utf8',
                'indent': 4,
                'overwrite': True
            }
        }
    }

    def parse(self, response):
        item = McdonaldsProductInfoItem()
        
        data = json.loads(response.text)
        
        item['name'] = data.get('item').get('item_name').replace('®', '')
        item['description'] = data.get('item').get('description')
        
        nutrition = data.get('item').get('nutrient_facts').get('nutrient')
        
        for nutrient in nutrition:
            if nutrient['nutrient_name_id'] == 'primary_serving_size':
                item['portion'] = f"{nutrient['value']} {nutrient['uom_description']}"
            elif nutrient['nutrient_name_id'] == 'energy_kcal':
                item['calories'] = f"{nutrient['value']} {nutrient['uom_description']}"
            elif nutrient['nutrient_name_id'] == 'fat':
                item['fats'] = f"{nutrient['value']} {nutrient['uom_description']}"
            elif nutrient['nutrient_name_id'] == 'carbohydrate':
                item['carbs'] = f"{nutrient['value']} {nutrient['uom_description']}"
            elif nutrient['nutrient_name_id'] == 'protein':
                item['proteins'] = f"{nutrient['value']} {nutrient['uom_description']}"
            elif nutrient['nutrient_name_id'] == 'НЖК':
                item['unsaturated_fats'] = f"{nutrient['value']} {nutrient['uom_description']}"
            elif nutrient['nutrient_name_id'] == 'Цукор':
                item['sugars'] = f"{nutrient['value']} {nutrient['uom_description']}"
            elif nutrient['nutrient_name_id'] == 'salt':
                item['salt'] = f"{nutrient['value']} {nutrient['uom_description']}"
        
        yield item