# Generated by Django 3.0.2 on 2020-01-12 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200112_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='company_contact',
            new_name='company_contact_id',
        ),
    ]
