# Generated by Django 4.1.6 on 2023-10-28 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('istedad', '0002_alter_buraxilis11_f1_a27_alter_buraxilis11_f1_a28_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buraxilis11',
            name='f1_d_q',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='buraxilis11',
            name='f2_d_q',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='buraxilis11',
            name='f3_d_k',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='buraxilis11',
            name='f3_d_q',
            field=models.IntegerField(default=0),
        ),
    ]
