# Generated by Django 4.2.4 on 2023-08-20 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ('created_at',)},
        ),
    ]
