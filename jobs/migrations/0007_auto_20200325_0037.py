# Generated by Django 2.2.7 on 2020-03-24 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_contact_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='title',
            new_name='email',
        ),
    ]
