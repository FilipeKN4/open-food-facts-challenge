from django.contrib.auth.models import User, Group
from rest_framework import serializers
from products import models


class ProductsSerializer(serializers.ModelSerializer):
    local_url = serializers.SerializerMethodField('product_local_url')
    created_t = serializers.DateTimeField(format="%s", required=False, read_only=True)
    last_modified_t = serializers.DateTimeField(format="%s", required=False, read_only=True)
    
    def product_local_url(self, obj):
        if 'request' in self.context:
            return self.context["request"].build_absolute_uri("{}/".format(obj.code))
        else:
            return ''
      
    class Meta:
        model = models.Products
        fields = (
            'id',
            'local_url',
            'code', 
            'status',
            'imported_t',
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
            'image_url',
        )
        

class ProductsUpdateHistorySerializer(serializers.ModelSerializer):
    local_url = serializers.SerializerMethodField('product_update_history_local_url')
    
    def product_update_history_local_url(self, obj):
        if 'request' in self.context:
            return self.context["request"].build_absolute_uri("{}/".format(obj.id))
        else:
            return ''
        
    class Meta:
        model = models.ProductsUpdateHistory
        fields = '__all__'