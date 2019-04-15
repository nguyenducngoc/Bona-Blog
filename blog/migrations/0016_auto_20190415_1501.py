# Generated by Django 2.2 on 2019-04-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190415_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='facebook_url',
            field=models.CharField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github_url',
            field=models.CharField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter_url',
            field=models.CharField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True),
        ),
    ]
