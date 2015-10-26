# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_purchase_date',
            field=models.CharField(max_length=15, blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_purchase_heure',
            field=models.CharField(max_length=15, blank=True),
        ),
    ]
