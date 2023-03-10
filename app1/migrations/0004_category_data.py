# Generated by Django 4.0.4 on 2022-11-21 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_registeration_data_delete_sample_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='category_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Profile')),
            ],
        ),
    ]
