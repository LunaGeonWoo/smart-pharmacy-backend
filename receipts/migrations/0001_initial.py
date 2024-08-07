# Generated by Django 5.0.6 on 2024-07-09 11:55

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicines', '0004_alter_medicine_price_alter_medicine_remaining'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_at', models.DateTimeField(auto_now_add=True, verbose_name='구매 시각')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='주인')),
            ],
        ),
        migrations.CreateModel(
            name='PastMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='개수')),
                ('price_per_medicine_at_purchase', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='구매 당시 하나 당 가격')),
                ('medicine', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='medicines.medicine', verbose_name='약')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='past_medicine', to='receipts.receipt')),
            ],
        ),
    ]
