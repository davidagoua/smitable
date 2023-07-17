# Generated by Django 4.1.7 on 2023-07-17 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0011_alter_constante_user_alter_consultation_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniteHospitalisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('capacite', models.PositiveIntegerField(default=1)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hospitalisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('details', models.JSONField(blank=True, null=True)),
                ('state', models.PositiveIntegerField(default=0)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient')),
                ('unite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.unitehospitalisation')),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
