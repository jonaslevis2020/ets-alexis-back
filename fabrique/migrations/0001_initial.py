# Generated by Django 4.2.6 on 2024-02-06 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ets_alexis.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.CharField(default=ets_alexis.utils.get_uuid, editable=False, max_length=8, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Titre/Intitule/Nom')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Date de Creation')),
                ('last_modified', models.DateField(auto_now=True, verbose_name='Derniere Modification')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Autheur')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.TextField(blank=True, max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('cni', models.CharField(max_length=50)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Adresse mail')),
                ('phone', models.CharField(max_length=20, verbose_name='numero de telephone')),
                ('address', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('Gerant', 'Gerant'), ('Fabricant', 'Fabricant'), ('Chauffeur', 'chauffeur'), ('Manutentionnaire', 'Manutentionnaire')], max_length=50)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Outil',
            fields=[
                ('id', models.CharField(default=ets_alexis.utils.get_uuid, editable=False, max_length=8, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('stock', models.IntegerField()),
                ('price', models.IntegerField()),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prestataire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('siteWeb', models.CharField(blank=True, max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('role', models.CharField(choices=[('Representant', 'Representant'), ('Responsable', 'Responsable')], max_length=50)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.CharField(default=ets_alexis.utils.get_uuid, editable=False, max_length=8, primary_key=True, serialize=False)),
                ('variation_category', models.CharField(choices=[('longueur', 'longueur'), ('largeur', 'largeur'), ('diametre', 'diametre'), ('forme', 'forme')], max_length=50, verbose_name='Type de variation')),
                ('description', models.TextField(blank=True, max_length=250, verbose_name='Description')),
                ('variation_value', models.CharField(max_length=50, verbose_name='Valeur de la variation')),
                ('stock', models.IntegerField(default=0, verbose_name='Quantite en Stock')),
                ('price', models.IntegerField(default=0, verbose_name='Prix Unitaire(en FCFA)')),
                ('is_active', models.BooleanField(default=True, verbose_name='Est actif')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True, verbose_name='Derniere modification')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='fabrique.article')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Auteur')),
            ],
        ),
        migrations.CreateModel(
            name='RepresentantPrestataire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.TextField(blank=True, max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('cni', models.CharField(max_length=50)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('prestataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='representants', to='fabrique.prestataire')),
            ],
        ),
        migrations.CreateModel(
            name='RepresentantClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.TextField(blank=True, max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('cni', models.CharField(max_length=50)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='representants', to='fabrique.client')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoRepresentantPrestataire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=250)),
                ('picture', models.ImageField(blank=True, upload_to='photos/prestataires/representants')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('representant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='fabrique.representantprestataire')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoRepresentantClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=250)),
                ('picture', models.ImageField(blank=True, upload_to='photos/clients/representants')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('representant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='fabrique.representantclient')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoPrestataire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=250)),
                ('picture', models.ImageField(blank=True, upload_to='photos/prestataires')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('representant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='fabrique.prestataire')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoOutil',
            fields=[
                ('id', models.CharField(default=ets_alexis.utils.get_uuid, editable=False, max_length=8, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, max_length=250)),
                ('picture', models.ImageField(blank=True, upload_to='photos/Outils')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('representant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='fabrique.outil')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoEmployer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=250)),
                ('picture', models.ImageField(blank=True, upload_to='photos/Employers')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='fabrique.employer')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=250)),
                ('picture', models.ImageField(blank=True, upload_to='photos/clients')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('representant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='fabrique.client')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoArticle',
            fields=[
                ('id', models.CharField(default=ets_alexis.utils.get_uuid, editable=False, max_length=8, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, max_length=250, verbose_name='Decription')),
                ('picture', models.ImageField(blank=True, upload_to='photos/Articles/', verbose_name='Image/Photo')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Date de creation')),
                ('last_modified', models.DateField(auto_now=True, verbose_name='Derniere modification')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='fabrique.article', verbose_name="Choix de l'article")),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Auteur')),
            ],
        ),
    ]
