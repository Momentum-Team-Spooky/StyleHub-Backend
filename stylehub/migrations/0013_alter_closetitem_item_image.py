# Generated by Django 4.0 on 2022-10-19 16:56

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stylehub', '0012_remove_closetitem_item_choice_closetitem_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closetitem',
            name='item_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='closet_items'),
        ),
    ]
