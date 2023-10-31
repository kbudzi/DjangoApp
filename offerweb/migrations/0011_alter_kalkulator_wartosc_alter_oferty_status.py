# Generated by Django 4.1.6 on 2023-10-30 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerweb', '0010_kalkulator_waga_alter_indeksy_czy_mat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kalkulator',
            name='wartosc',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='oferty',
            name='status',
            field=models.PositiveBigIntegerField(choices=[(1, 'w trakcie'), (3, 'wysłana'), (0, 'nowa'), (2, 'opracowana')], default=0),
        ),
    ]