# Generated by Django 3.0.5 on 2021-08-26 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_App', '0002_usertable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prodtable',
            old_name='customer_name',
            new_name='name',
        ),
    ]