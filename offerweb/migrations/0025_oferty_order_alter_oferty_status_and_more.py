# Generated by Django 4.1.6 on 2023-08-08 07:25

from django.db import migrations, models
import offerweb.fields


class Migration(migrations.Migration):

    dependencies = [
        ('offerweb', '0024_alter_oferty_status_alter_operacje_typ_operacji'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferty',
            name='order',
            field=offerweb.fields.OrderField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='oferty',
            name='status',
            field=models.PositiveBigIntegerField(choices=[(0, 'nowa'), (1, 'w trakcie'), (2, 'opracowana'), (3, 'wysłana')], default=0),
        ),
        migrations.AlterField(
            model_name='operacje',
            name='typ_operacji',
            field=models.PositiveBigIntegerField(choices=[(1, 'Kooperacja'), (0, 'Zwykła')], default=0),
        ),
    ]