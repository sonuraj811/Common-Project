# Generated by Django 4.0.4 on 2022-11-04 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sample_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Age', models.IntegerField(blank=True, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
