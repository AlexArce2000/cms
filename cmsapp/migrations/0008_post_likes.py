# Generated by Django 4.2.4 on 2023-08-13 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_alter_userprofile_about'),
        ('cmsapp', '0007_rename_writter_post_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blog_post', to='userprofile.userprofile'),
        ),
    ]