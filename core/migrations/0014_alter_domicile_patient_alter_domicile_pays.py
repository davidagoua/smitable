# Generated by Django 4.1.7 on 2023-07-17 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_patient_commune_remove_patient_quartier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domicile',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domiciles', to='core.patient'),
        ),
        migrations.AlterField(
            model_name='domicile',
            name='pays',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
