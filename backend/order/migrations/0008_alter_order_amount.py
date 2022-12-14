# Generated by Django 3.2.3 on 2021-07-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_order_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, error_messages={'name': {'max_length': 'The price must be between 0.01 and the price of the product'}}, help_text='Maximum is the price of the product.', max_digits=8, null=True, verbose_name='Amount to offer'),
        ),
    ]
