# Generated by Django 4.1.6 on 2023-10-17 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offerweb', '0005_alter_indeksy_czy_mat_alter_indeksy_kontrahent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gatunek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(blank=True, max_length=30)),
                ('gestosc', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Mytechno',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('offerweb.technologia',),
        ),
        migrations.AlterField(
            model_name='oferty',
            name='status',
            field=models.PositiveBigIntegerField(choices=[(3, 'wysłana'), (1, 'w trakcie'), (0, 'nowa'), (2, 'opracowana')], default=0),
        ),
        migrations.AlterField(
            model_name='operacje',
            name='typ_operacji',
            field=models.PositiveBigIntegerField(choices=[(0, 'Zwykła'), (1, 'Kooperacja')], default=0),
        ),
        migrations.AlterField(
            model_name='technologia',
            name='operacja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='offerweb.operacje'),
        ),
        migrations.CreateModel(
            name='Kalkulator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profil', models.PositiveBigIntegerField(choices=[(0, 'Wałek'), (1, 'Blacha')], default=0)),
                ('srednica', models.DecimalField(decimal_places=2, max_digits=6)),
                ('szerokosc', models.DecimalField(decimal_places=2, max_digits=6)),
                ('grubosc', models.DecimalField(decimal_places=2, max_digits=6)),
                ('dlugosc', models.DecimalField(decimal_places=2, max_digits=6)),
                ('gatunek', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='offerweb.gatunek')),
            ],
        ),
    ]
