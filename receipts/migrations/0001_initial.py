# Generated by Django 5.0.6 on 2024-05-26 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='구매 시각')),
                ('medicine', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='medicines.medicine', verbose_name='약')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
