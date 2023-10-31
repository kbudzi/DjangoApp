# Generated by Django 4.1.6 on 2023-10-30 09:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('offerweb', '0008_alter_kalkulator_dlugosc_alter_kalkulator_gatunek_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kalkulator',
            name='wartosc',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='indeksy',
            name='czy_mat',
            field=models.PositiveBigIntegerField(choices=[(0, 'Tak'), (1, 'Nie')], default=1),
        ),
        migrations.AlterField(
            model_name='kalkulator',
            name='profil',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='oferty',
            name='status',
            field=models.PositiveBigIntegerField(choices=[(1, 'w trakcie'), (3, 'wysłana'), (0, 'nowa'), (2, 'opracowana')], default=0),
        ),
        migrations.AlterField(
            model_name='operacje',
            name='typ_operacji',
            field=models.PositiveBigIntegerField(choices=[(1, 'Kooperacja'), (0, 'Zwykła')], default=0),
        ),
    ]
