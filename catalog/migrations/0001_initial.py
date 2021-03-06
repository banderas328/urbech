# Generated by Django 2.0.2 on 2019-01-06 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalogTitle', models.CharField(max_length=250)),
                ('catalogText', models.TextField()),
                ('catalogImage', models.ImageField(upload_to='images/')),
                ('catalogGramms', models.CharField(max_length=250)),
                ('catalogCost', models.CharField(max_length=250)),
            ],
        ),
    ]
