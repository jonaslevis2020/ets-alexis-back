# Generated by Django 4.2.6 on 2024-01-28 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabrique', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='price',
        ),
        migrations.RemoveField(
            model_name='article',
            name='stock',
        ),
        migrations.AddField(
            model_name='variation',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Prix Unitaire(en FCFA)'),
        ),
        migrations.AddField(
            model_name='variation',
            name='stock',
            field=models.IntegerField(default=0, verbose_name='Quantite en Stock'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='variation_value',
            field=models.CharField(max_length=50, unique=True, verbose_name='Valeur de la variation'),
        ),
    ]