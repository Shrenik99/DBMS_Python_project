# Generated by Django 3.1.5 on 2021-02-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20210203_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]