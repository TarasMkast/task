# Generated by Django 3.0.8 on 2020-07-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findplace', '0003_objtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objtype',
            name='objtype',
            field=models.CharField(choices=[('Cafe', 'cafe'), ('Hospital', 'hospital'), ('Police', 'police')], max_length=20),
        ),
    ]
