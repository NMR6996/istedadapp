# Generated by Django 4.1.6 on 2023-12-02 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('istedad', '0029_alter_asagisinif_ata_adi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blok11',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sinaq_no', models.CharField(max_length=100)),
                ('aad', models.CharField(max_length=12)),
                ('soyad', models.CharField(max_length=12)),
                ('is_no', models.CharField(max_length=6)),
                ('sinif', models.CharField(max_length=2)),
                ('blok', models.CharField(max_length=1)),
                ('cem', models.FloatField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='sinaqlar',
            name='sinaq_adi',
            field=models.CharField(max_length=50, verbose_name='Sınaq adı'),
        ),
    ]
