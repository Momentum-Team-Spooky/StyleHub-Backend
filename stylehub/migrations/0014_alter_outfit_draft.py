# Generated by Django 4.0 on 2022-10-22 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stylehub', '0013_alter_closetitem_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]
