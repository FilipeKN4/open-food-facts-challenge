from djongo import models

class Products(models.Model):
    class Status(models.TextChoices):
        draft = 'draft'
        trash = 'trash'
        published = 'published'
        
    id = models.ObjectIdField()
    code = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=9, choices=Status.choices)
    imported_t = models.DateTimeField(auto_now_add=True)
    url = models.URLField(blank=True, null=True)
    creator = models.TextField(blank=True, null=True)
    created_t = models.DateTimeField(blank=True, null=True)
    last_modified_t = models.DateTimeField(blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    quantity = models.TextField(blank=True, null=True)
    brands = models.TextField(blank=True, null=True)
    categories = models.TextField(blank=True, null=True)
    labels = models.TextField(blank=True, null=True)
    cities = models.TextField(blank=True, null=True)
    purchase_places = models.TextField(blank=True, null=True)
    stores = models.TextField(blank=True, null=True)
    ingredients_text = models.TextField(blank=True, null=True)
    traces = models.TextField(blank=True, null=True)
    serving_size = models.TextField(blank=True, null=True)
    serving_quantity = models.DecimalField(default=0.0, decimal_places=1, max_digits=10, blank=True)
    nutriscore_score = models.IntegerField(blank=True, null=True)
    nutriscore_grade = models.CharField(max_length=1, blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)