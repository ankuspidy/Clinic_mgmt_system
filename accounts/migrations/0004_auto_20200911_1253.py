# Generated by Django 2.1.7 on 2020-09-11 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_accounts_joining_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='joining_date',
            field=models.DateField(auto_now=True),
        ),
    ]