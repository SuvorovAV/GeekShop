<<<<<<< HEAD
# Generated by Django 2.2.17 on 2021-02-04 17:53
=======
# Generated by Django 2.2.18 on 2021-02-08 17:06
>>>>>>> master

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ("mainapp", "0001_initial"),
=======
        ('mainapp', '0001_initial'),
>>>>>>> master
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name="Product",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=128, verbose_name="имя продукта")),
                ("image", models.ImageField(blank=True, upload_to="products_images")),
                ("short_desc", models.CharField(blank=True, max_length=60, verbose_name="краткое описание продукта")),
                ("description", models.TextField(blank=True, verbose_name="описание продукта")),
                ("price", models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name="цена продукта")),
                ("quantity", models.PositiveIntegerField(default=0, verbose_name="количество на складе")),
                (
                    "category",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="mainapp.ProductCategory"),
                ),
=======
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='имя продукта')),
                ('image', models.ImageField(blank=True, upload_to='products_images')),
                ('short_desc', models.CharField(blank=True, max_length=60, verbose_name='краткое описание продукта')),
                ('description', models.TextField(blank=True, verbose_name='описание продукта')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='цена продукта')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='количество на складе')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductCategory')),
>>>>>>> master
            ],
        ),
    ]
