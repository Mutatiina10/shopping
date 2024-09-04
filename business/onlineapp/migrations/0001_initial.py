# Generated by Django 5.1 on 2024-09-04 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.IntegerField()),
                ('product_quantity', models.IntegerField()),
                ('product_description', models.TextField()),
                ('product_category', models.CharField(max_length=100)),
                ('product_comment', models.TextField(max_length=100)),
                ('product_image', models.ImageField(upload_to='images/')),
                ('product_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
