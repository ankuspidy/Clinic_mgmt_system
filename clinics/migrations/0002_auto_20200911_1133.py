# Generated by Django 2.1.7 on 2020-09-11 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clinics',
            old_name='clinic_admin',
            new_name='accounts',
        ),
    ]
