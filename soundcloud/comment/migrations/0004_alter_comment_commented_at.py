# Generated by Django 3.2.6 on 2022-01-02 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_merge_0002_alter_comment_parent_comment_0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commented_at',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
