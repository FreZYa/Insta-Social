# Generated by Django 4.2.23 on 2025-06-12 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_by',
            field=models.CharField(default='admin', max_length=200),
            preserve_default=False,
        ),
    ]
