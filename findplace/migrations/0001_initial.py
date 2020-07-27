# Generated by Django 3.0.8 on 2020-07-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='е-пошта')),
                ('type_object', models.CharField(max_length=10, verbose_name='обєкт пошуку')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публікації')),
            ],
            options={
                'verbose_name': 'Історія пошуку',
                'verbose_name_plural': 'Історія пошуку',
                'ordering': ['-published'],
            },
        ),
    ]