# Generated by Django 3.1.3 on 2020-11-05 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='lineons',
            new_name='linenos',
        ),
    ]
