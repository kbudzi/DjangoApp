# Generated by Django 4.1.6 on 2023-09-25 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerweb', '0033_alter_oferty_status_alter_operacje_typ_operacji'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontrahent',
            name='ulica',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='oferty',
            name='status',
            field=models.PositiveBigIntegerField(choices=[(0, 'nowa'), (1, 'w trakcie'), (3, 'wysłana'), (2, 'opracowana')], default=0),
        ),
    ]