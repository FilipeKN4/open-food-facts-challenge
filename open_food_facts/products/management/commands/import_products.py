import gzip
import json
from decimal import Decimal
from datetime import datetime
from django.utils.timezone import make_aware
from django.core.management.base import BaseCommand, CommandError
from products.models import Products

class Command(BaseCommand):
    help = 'Import products from gave file'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+', type=str)

    def handle(self, *args, **options):
        for file in options['file']:
            try:
                print(file)
                json_content = []
                with gzip.open('./all_products/{}'.format(file), 'r') as gzip_file:
                    for line in gzip_file:
                        line = line.rstrip()
                        if line:
                            obj = json.loads(line)
                            json_content.append(obj)
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
                fields_dict = {}
                for field in fields:
                    if len(product_json.get(field).split('"')) > 1:
                        fields_dict[field] = product_json.get(field).split('"')[1]
                    elif product_json.get(field) == '"':
                        fields_dict[field] = ''
                    else:
                        fields_dict[field] = product_json.get(field)
                                    
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
                        serving_quantity=Decimal(fields_dict['serving_quantity']) if fields_dict['serving_quantity'] != '' else 0,
                        nutriscore_score=int(fields_dict['nutriscore_score']) if fields_dict['serving_quantity'] != '' else 0,
                        nutriscore_grade=fields_dict['nutriscore_grade'],
                        main_category=fields_dict['main_category'],
                        image_url=fields_dict['image_url']
                    )
                else:
                    print('Product with code "%s" already exists' % fields_dict['code'])