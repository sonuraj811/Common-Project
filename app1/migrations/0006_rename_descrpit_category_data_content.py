# Generated by Django 4.0.4 on 2022-11-21 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_rename_description_category_data_descrpit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category_data',
            old_name='descrpit',
            new_name='content',
        ),
    ]
