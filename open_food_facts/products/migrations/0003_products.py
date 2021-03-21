# Generated by Django 3.0 on 2021-03-21 00:31

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_delete_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('code', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('trash', 'Trash'), ('published', 'Published')], max_length=9)),
                ('imported_t', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('creator', models.TextField(blank=True, null=True)),
                ('created_t', models.DateTimeField(blank=True, null=True)),
                ('last_modified_t', models.DateTimeField(blank=True, null=True)),
                ('product_name', models.TextField(blank=True, null=True)),
                ('quantity', models.TextField(blank=True, null=True)),
                ('brands', models.TextField(blank=True, null=True)),
                ('categories', models.TextField(blank=True, null=True)),
                ('labels', models.TextField(blank=True, null=True)),
                ('cities', models.TextField(blank=True, null=True)),
                ('purchase_places', models.TextField(blank=True, null=True)),
                ('stores', models.TextField(blank=True, null=True)),
                ('ingredients_text', models.TextField(blank=True, null=True)),
                ('traces', models.TextField(blank=True, null=True)),
                ('serving_size', models.TextField(blank=True, null=True)),
                ('serving_quantity', models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=10)),
                ('nutriscore_score', models.IntegerField(blank=True, null=True)),
                ('nutriscore_grade', models.CharField(blank=True, max_length=1, null=True)),
                ('main_category', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
