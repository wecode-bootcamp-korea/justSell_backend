# Generated by Django 3.0.2 on 2020-01-15 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20200116_0526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invitationcodes',
            old_name='invitation_code',
            new_name='invitation_codes',
        ),
    ]
