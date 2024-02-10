# Generated by Django 4.2.6 on 2024-02-10 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabrique', '0002_alter_outil_title_alter_photooutil_representant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='cni',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='photoclient',
            name='picture',
            field=models.ImageField(upload_to='photos/clients'),
        ),
        migrations.AlterField(
            model_name='photorepresentantclient',
            name='picture',
            field=models.ImageField(upload_to='photos/clients/representants'),
        ),
        migrations.AlterField(
            model_name='representantclient',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='representantclient',
            name='cni',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='representantclient',
            name='phone',
            field=models.TextField(max_length=20),
        ),
    ]