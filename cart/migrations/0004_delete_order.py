# Generated by Django 4.1 on 2022-09-19 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_order_address_alter_order_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]