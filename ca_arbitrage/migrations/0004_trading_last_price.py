# Generated by Django 3.1.1 on 2021-04-18 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca_arbitrage', '0003_userkeys'),
    ]

    operations = [
        migrations.AddField(
            model_name='trading',
            name='last_price',
            field=models.FloatField(default=0, null=True, verbose_name='Цена'),
        ),
    ]