# Generated by Django 3.0 on 2021-03-19 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='imported_t',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='nutriscore_grade',
            field=models.CharField(max_length=1),
        ),
    ]