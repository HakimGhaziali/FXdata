# Generated by Django 4.0.6 on 2022-08-01 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_post_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload',
            field=models.ImageField(blank=True, upload_to='upload/'),
        ),
    ]
