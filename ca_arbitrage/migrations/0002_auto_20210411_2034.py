# Generated by Django 3.1.1 on 2021-04-11 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ca_arbitrage', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BinanceLivecoin',
        ),
        migrations.DeleteModel(
            name='BittrexLivecoin',
        ),
        migrations.DeleteModel(
            name='HitbtcLivecoin',
        ),
        migrations.DeleteModel(
            name='KucoinLivecoin',
        ),
        migrations.DeleteModel(
            name='Livecoin',
        ),
        migrations.DeleteModel(
            name='LivecoinBibox',
        ),
        migrations.DeleteModel(
            name='LivecoinBitz',
        ),
        migrations.DeleteModel(
            name='LivecoinCoinex',
        ),
        migrations.DeleteModel(
            name='LivecoinGateio',
        ),
        migrations.DeleteModel(
            name='LivecoinHuobi',
        ),
        migrations.DeleteModel(
            name='LivecoinKraken',
        ),
        migrations.DeleteModel(
            name='LivecoinOkex',
        ),
        migrations.DeleteModel(
            name='PoloniexLivecoin',
        ),
    ]