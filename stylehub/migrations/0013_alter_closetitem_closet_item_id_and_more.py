# Generated by Django 4.0 on 2022-10-15 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stylehub', '0012_genericstringtaggedclosetitem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closetitem',
            name='closet_item_id',
            field=models.CharField(default='None', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='outfit_id',
            field=models.CharField(default='None', max_length=50, primary_key=True, serialize=False),
        ),
    ]
