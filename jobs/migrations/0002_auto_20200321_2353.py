# Generated by Django 2.2.7 on 2020-03-21 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='title', max_length=140),
        ),
        migrations.AddField(
            model_name='job',
            name='used_tech',
            field=models.CharField(default='Skils', max_length=140),
        ),
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.TextField(max_length=400),
        ),
    ]
