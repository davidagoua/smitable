# Generated by Django 4.1.7 on 2023-07-22 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_boxhospitalisation_chambre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalisation',
            name='unite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.boxhospitalisation'),
        ),
    ]