# Generated by Django 4.1.7 on 2023-07-17 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratoire', '0009_analysepatient_technique_analyse_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysepatient',
            name='analyse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='laboratoire.analyse'),
        ),
    ]
