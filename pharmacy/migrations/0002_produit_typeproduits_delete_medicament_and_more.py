# Generated by Django 4.1.7 on 2023-07-17 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('reference', models.CharField(max_length=200)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('prix', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeProduits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Medicament',
        ),
        migrations.RenameModel(
            old_name='CategoryMedicament',
            new_name='CategoryProduits',
        ),
        migrations.AddField(
            model_name='produit',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.categoryproduits'),
        ),
        migrations.AddField(
            model_name='produit',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.typeproduits'),
        ),
    ]
