# Generated by Django 4.1.4 on 2022-12-14 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_catalog', '0002_remove_tag_snippet_snippet_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='tag',
            new_name='tags',
        ),
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(max_length=100),
        ),
    ]