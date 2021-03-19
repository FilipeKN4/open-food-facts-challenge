from djongo import models

class Products(models.Model):
    class Status(models.TextChoices):
        draft = 'draft'
        trash = 'trash'
        published = 'published'
        
    id = models.ObjectIdField()
    code = models.IntegerField()
    status = models.CharField(max_length=9, choices=Status.choices)
    imported_t = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
    creator = models.TextField(blank=True)
    created_at = models.DateTimeField()
    last_modified_t = models.DateTimeField()
    product_name = models.TextField(blank=True)
    quantity = models.TextField(blank=True)
    brands = models.TextField(blank=True)
    categories = models.TextField(blank=True)
    labels = models.TextField(blank=True)
    cities = models.TextField(blank=True)
    purchase_places = models.TextField(blank=True)
    stores = models.TextField(blank=True)
    ingredients_text = models.TextField(blank=True)
    traces = models.TextField(blank=True)
    serving_size = models.TextField(blank=True)
    nutriscore_score = models.DecimalField(decimal_places=1, max_digits=10)
    nutriscore_grade = models.CharField(max_length=1)
    main_category = models.TextField(blank=True)
    image_url = models.URLField()