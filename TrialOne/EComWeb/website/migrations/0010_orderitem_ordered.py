# Generated by Django 3.1.5 on 2021-03-06 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_remove_orderitem_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
