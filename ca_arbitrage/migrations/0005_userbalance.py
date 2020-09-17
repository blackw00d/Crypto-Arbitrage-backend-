# Generated by Django 3.1.1 on 2020-09-17 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca_arbitrage', '0004_poloniexhitbtc'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default=None, max_length=50, null=True, verbose_name='Имя')),
                ('balance', models.TextField(default=None, null=True, verbose_name='Баланс')),
                ('totalbtc', models.FloatField(default=None, null=True, verbose_name='TotalBTC')),
                ('totalusd', models.FloatField(default=None, null=True, verbose_name='TotalUSD')),
            ],
        ),
    ]