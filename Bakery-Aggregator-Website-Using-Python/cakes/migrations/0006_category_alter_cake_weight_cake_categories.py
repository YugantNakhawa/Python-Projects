# Generated by Django 5.0 on 2024-02-07 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0005_rename_title_cake_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='cake',
            name='weight',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='cake',
            name='categories',
            field=models.ManyToManyField(to='cakes.category'),
        ),
    ]