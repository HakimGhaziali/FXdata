# Generated by Django 4.0.6 on 2022-08-01 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_alter_review_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='author',
            new_name='authorreview',
        ),
    ]