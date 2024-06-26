# Generated by Django 5.0.4 on 2024-04-28 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_book_buy_amount_book_rent_amount_book_rented_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_description',
            field=models.TextField(max_length=225),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='cur_book',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='fav_author',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='fav_book',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='fav_genres',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='profile_description',
            field=models.TextField(max_length=225, null=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.TextField(max_length=225)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.book')),
            ],
        ),
    ]
