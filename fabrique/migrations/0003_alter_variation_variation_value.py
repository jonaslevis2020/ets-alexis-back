# Generated by Django 4.2.6 on 2024-01-28 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabrique', '0002_remove_article_price_remove_article_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_value',
            field=models.CharField(max_length=50, verbose_name='Valeur de la variation'),
        ),
    ]