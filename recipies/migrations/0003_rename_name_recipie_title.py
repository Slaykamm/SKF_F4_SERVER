# Generated by Django 4.0 on 2021-12-18 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0002_remove_category_category_recipie_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipie',
            old_name='name',
            new_name='title',
        ),
    ]
