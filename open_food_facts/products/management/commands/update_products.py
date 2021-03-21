# Django imports
from django.core.management.base import BaseCommand, CommandError

# Products app imports
from products.models import Products, ProductsUpdateHistory
from products.views import get_product, update_product

class Command(BaseCommand):
    help = 'Update or Delete products'
    
    def handle(self, *args, **options):
        created_products = 0
        updated_products = 0
        deleted_products = 0
        
        products = Products.objects.all()
        
        for product in products:
            data = get_product(product.code)
            product_json = data.get('product')
            if product_json:
                product = update_product(product_json, product)
                
                updated_products += 1
                
                print('Product with code "%s" successfully updated' % product.code)
            
            else:
                product.status = Products.Status.trash
                product.save()
                
                deleted_products += 1
                
                print('Product with code "%s" successfully deleted' % product.code)

        ProductsUpdateHistory.objects.create(
            created_products = created_products,
            updated_products = updated_products,
            deleted_products = deleted_products
        )