# Generated by Django 3.1.7 on 2021-04-05 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_head_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file_upload',
            field=models.FileField(blank=True, upload_to='blog/files/%Y/%m/%d'),
        ),
    ]
