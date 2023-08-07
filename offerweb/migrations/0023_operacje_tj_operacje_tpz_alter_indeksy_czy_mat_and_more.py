# Generated by Django 4.1.6 on 2023-08-04 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerweb', '0022_technologia_indeks_alter_indeksy_czy_mat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='operacje',
            name='tj',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='operacje',
            name='tpz',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='indeksy',
            name='czy_mat',
            field=models.PositiveBigIntegerField(choices=[(0, 'Tak'), (1, 'Nie')], default=1),
        ),
        migrations.AlterField(
            model_name='oferty',
            name='status',
            field=models.PositiveBigIntegerField(choices=[(1, 'w trakcie'), (3, 'wysłana'), (2, 'opracowana'), (0, 'nowa')], default=0),
        ),
    ]
