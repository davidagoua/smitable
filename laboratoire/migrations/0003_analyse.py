# Generated by Django 4.1.7 on 2023-07-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratoire', '0002_protocolanalyse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analyse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
    ]