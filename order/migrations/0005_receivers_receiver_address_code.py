# Generated by Django 3.0.2 on 2020-01-14 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20200113_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='receivers',
            name='receiver_address_code',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
