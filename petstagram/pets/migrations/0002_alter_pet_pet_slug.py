# Generated by Django 3.2.18 on 2023-02-25 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]