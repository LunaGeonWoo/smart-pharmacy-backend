# Generated by Django 5.0.6 on 2024-05-14 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='구매 시각'),
        ),
    ]
