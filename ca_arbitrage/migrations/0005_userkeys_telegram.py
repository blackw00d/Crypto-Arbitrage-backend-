# Generated by Django 3.1.1 on 2021-04-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca_arbitrage', '0004_trading_last_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='userkeys',
            name='telegram',
            field=models.CharField(default=None, max_length=30, null=True, verbose_name='Telegram'),
        ),
    ]
