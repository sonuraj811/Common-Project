# Generated by Django 4.0.4 on 2022-11-04 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample_data',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='sample_data',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='sample_data',
            old_name='Name',
            new_name='name',
        ),
    ]
