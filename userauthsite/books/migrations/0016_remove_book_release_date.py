# Generated by Django 5.0.4 on 2024-05-09 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_alter_book_release_date_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='release_date',
        ),
    ]