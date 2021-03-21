# Libs imports
import gzip
import json
from decimal import Decimal
from datetime import datetime

# Django imports
from django.utils.timezone import make_aware
from django.core.management.base import BaseCommand, CommandError

# Products app imports
from products.models import Products, ProductsUpdateHistory
from products.views import get_product, update_product

class Command(BaseCommand):
    help = 'Import, Update or Delete products from gave file'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+', type=str)
        

    def get_cleaned_fields(self, product_json, fields):
        fields_dict = {}
        for field in fields:
            if len(product_json.get(field).split('"')) > 1:
                fields_dict[field] = product_json.get(field).split('"')[1]
            elif product_json.get(field) == '"':
                fields_dict[field] = ''
            else:
                fields_dict[field] = product_json.get(field)
                
        return fields_dict
    
    
    def handle(self, *args, **options):
        created_products = 0
        updated_products = 0
        deleted_products = 0
        for file in options['file']:
            try:
                print(file)
                json_content = []
                count = 0
                with gzip.open('./all_products/{}'.format(file), 'r') as gzip_file:
                    for line in gzip_file:
                        if count < 100:
                            line = line.rstrip()
                            if line:
                                obj = json.loads(line)
                                json_content.append(obj)
                        else:
                            break
                        count += 1
                        
            except:
                raise CommandError('File "%s" not found' % file)
            
            fields = [
                'code',
                'url',
                'creator',
                'created_t',
                'last_modified_t',
                'product_name',
                'quantity',
                'brands',
                'categories',
                'labels',
                'cities',
                'purchase_places',
                'stores',
                'ingredients_text',
                'traces',
                'serving_size',
                'serving_quantity',
                'nutriscore_score',
                'nutriscore_grade',
                'main_category',
                'image_url'
            ]

            for product_json in json_content:
                fields_dict = self.get_cleaned_fields(product_json, fields)
                                    
                if not Products.objects.filter(code=fields_dict['code']):
                    Products.objects.create(
                        code=fields_dict['code'],
                        status=Products.Status.draft,
                        url=fields_dict['url'],
                        creator=fields_dict['creator'],
                        created_t=make_aware(datetime.fromtimestamp(int(fields_dict['created_t']))),
                        last_modified_t=make_aware(datetime.fromtimestamp(int(fields_dict['last_modified_t']))),
                        product_name=fields_dict['product_name'],
                        quantity=fields_dict['quantity'],
                        brands=fields_dict['brands'],
                        categories=fields_dict['categories'],
                        labels=fields_dict['labels'],
                        cities=fields_dict['cities'],
                        purchase_places=fields_dict['purchase_places'],
                        stores=fields_dict['stores'],
                        ingredients_text=fields_dict['ingredients_text'],
                        traces=fields_dict['traces'],
                        serving_size=fields_dict['serving_size'],
                        serving_quantity= 0 if fields_dict['serving_quantity'] == '' else Decimal(fields_dict['serving_quantity']),
                        nutriscore_score= 0 if fields_dict['nutriscore_score'] == '' else int(fields_dict['nutriscore_score']),
                        nutriscore_grade=fields_dict['nutriscore_grade'],
                        main_category=fields_dict['main_category'],
                        image_url=fields_dict['image_url']
                    )
                    created_products += 1
                    
                    print('Product with code "%s" successfully created' % fields_dict['code'])
                else:
                    product = Products.objects.filter(code=fields_dict['code']).first()
                    if product:
                        data = get_product(product.code)
                        product_json = data.get('product')
                        if product_json:
                            product = update_product(product_json, product)
                            
                            updated_products += 1
                            
                            print('Product with code "%s" successfully updated' % fields_dict['code'])
                        
                        else:
                            product.status = Products.Status.trash
                            product.save()
                            
                            deleted_products += 1
                            
                            print('Product with code "%s" successfully deleted' % fields_dict['code'])

        ProductsUpdateHistory.objects.create(
            created_products = created_products,
            updated_products = updated_products,
            deleted_products = deleted_products
        )