# Generated by Django 4.1.6 on 2023-07-07 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerweb', '0015_alter_indeksy_czy_mat_alter_indeksy_ilosc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indeksy',
            name='czy_mat',
            field=models.PositiveBigIntegerField(choices=[(1, 'Nie'), (0, 'Tak')], default=1),
        ),
        migrations.AlterField(
            model_name='indeksy',
            name='ilosc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='oferty',
            name='status',
            field=models.PositiveBigIntegerField(choices=[(2, 'opracowana'), (3, 'wysłana'), (1, 'w trakcie'), (0, 'nowa')], default=0),
        ),
        migrations.AlterField(
            model_name='operacje',
            name='typ_operacji',
            field=models.PositiveBigIntegerField(choices=[(1, 'Kooperacja'), (0, 'Zwykła')], default=0),
        ),
    ]