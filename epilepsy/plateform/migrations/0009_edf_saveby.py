# Generated by Django 3.2 on 2021-05-15 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plateform', '0008_customer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='edf',
            name='saveBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plateform.customer'),
        ),
    ]
