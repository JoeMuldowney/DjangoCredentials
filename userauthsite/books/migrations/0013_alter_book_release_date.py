# Generated by Django 5.0.4 on 2024-05-09 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_book_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
