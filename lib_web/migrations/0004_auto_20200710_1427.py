# Generated by Django 3.0.5 on 2020-07-10 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lib_web', '0003_auto_20200426_1112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='ISBN',
            new_name='isbn',
        ),
    ]
