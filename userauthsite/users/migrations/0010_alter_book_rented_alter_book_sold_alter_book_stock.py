# Generated by Django 5.0.4 on 2024-04-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rented',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='sold',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
