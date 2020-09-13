# Generated by Django 3.1.1 on 2020-09-10 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca_arbitrage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BinanceHitbtc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50, null=True, verbose_name='Имя')),
                ('binance_price', models.CharField(default=None, max_length=50, null=True, verbose_name='Цена Binance')),
                ('hitbtc_price', models.CharField(default=None, max_length=50, null=True, verbose_name='Цена Bibox')),
                ('binance_volume', models.CharField(default=None, max_length=50, null=True, verbose_name='Объем Binance')),
                ('hitbtc_volume', models.CharField(default=None, max_length=50, null=True, verbose_name='Объем Bibox')),
                ('profit', models.FloatField(default=None, null=True, verbose_name='Профит')),
            ],
        ),
    ]
