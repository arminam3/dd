# Generated by Django 4.1 on 2022-09-30 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_n'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='n',
        ),
    ]