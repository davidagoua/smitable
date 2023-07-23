# Generated by Django 4.1.7 on 2023-07-22 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_categoriemaladies_maladie_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChambreHospitalisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('unite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.unitehospitalisation')),
            ],
        ),
        migrations.CreateModel(
            name='BoxHospitalisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacite', models.PositiveIntegerField(default=1)),
                ('nom', models.CharField(max_length=100)),
                ('occuper', models.BooleanField(default=False)),
                ('chambre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.chambrehospitalisation')),
            ],
        ),
    ]