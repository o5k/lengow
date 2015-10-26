# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marketplace', models.CharField(max_length=50)),
                ('order_id', models.CharField(max_length=50)),
                ('order_purchase_date', models.CharField(max_length=15)),
                ('order_purchase_heure', models.CharField(max_length=15)),
                ('order_amount', models.CharField(max_length=50)),
            ],
        ),
    ]
