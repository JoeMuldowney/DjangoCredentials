# Generated by Django 5.0.4 on 2024-05-12 18:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0024_alter_book_title'),
        ('users', '0012_remove_book_book_remove_review_review_delete_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225, null=True)),
                ('author', models.CharField(max_length=45, null=True)),
                ('user', models.IntegerField(null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
    ]
