# Generated by Django 4.1.7 on 2023-05-18 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM1', '0008_order_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
