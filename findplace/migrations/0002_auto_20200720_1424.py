# Generated by Django 3.0.8 on 2020-07-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findplace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='type_object',
            field=models.CharField(max_length=20, verbose_name='обєкт пошуку'),
        ),
    ]
