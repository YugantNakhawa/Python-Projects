# Generated by Django 5.0 on 2024-02-06 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0004_remove_cake_author_remove_cake_follow_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cake',
            old_name='title',
            new_name='name',
        ),
    ]
