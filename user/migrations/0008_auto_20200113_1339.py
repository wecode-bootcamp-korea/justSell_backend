# Generated by Django 3.0.2 on 2020-01-13 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_users_company_registeration_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_email',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
