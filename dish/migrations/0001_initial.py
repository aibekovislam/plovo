# Generated by Django 3.2 on 2021-04-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'блюдо',
                'verbose_name_plural': 'Блюда',
            },
        ),
    ]
