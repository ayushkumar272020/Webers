# Generated by Django 3.2.8 on 2021-11-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_customer_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AddField(
            model_name='shopkeeper',
            name='address',
            field=models.TextField(null=True),
        ),
    ]