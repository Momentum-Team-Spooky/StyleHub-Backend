# Generated by Django 4.0 on 2022-10-25 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stylehub', '0015_outfit_unique_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='draft',
            field=models.BooleanField(default=True),
        ),
    ]
