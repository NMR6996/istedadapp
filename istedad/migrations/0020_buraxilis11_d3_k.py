# Generated by Django 4.1.6 on 2023-10-29 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('istedad', '0019_alter_buraxilis11_options_alter_buraxilis11_cem'),
    ]

    operations = [
        migrations.AddField(
            model_name='buraxilis11',
            name='d3_k',
            field=models.CharField(default='', max_length=30),
        ),
    ]
