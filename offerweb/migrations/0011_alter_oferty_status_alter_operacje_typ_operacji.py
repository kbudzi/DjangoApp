# Generated by Django 4.1.6 on 2023-07-07 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerweb', '0010_alter_indeksy_czy_mat_alter_oferty_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferty',
            name='status',
            field=models.PositiveBigIntegerField(choices=[(2, 'opracowana'), (1, 'w trakcie'), (0, 'nowa'), (3, 'wysłana')], default=0),
        ),
        migrations.AlterField(
            model_name='operacje',
            name='typ_operacji',
            field=models.PositiveBigIntegerField(choices=[(1, 'Kooperacja'), (0, 'Zwykła')], default=0),
        ),
    ]