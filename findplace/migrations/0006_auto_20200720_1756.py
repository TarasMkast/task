# Generated by Django 3.0.8 on 2020-07-20 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('findplace', '0005_auto_20200720_1749'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='objtype',
            options={'ordering': ['objtype'], 'verbose_name': 'Тип місця пошуку', 'verbose_name_plural': 'Типи місця пошуку'},
        ),
    ]