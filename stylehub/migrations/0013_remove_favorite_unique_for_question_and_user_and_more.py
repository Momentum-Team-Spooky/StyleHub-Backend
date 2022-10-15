# Generated by Django 4.0 on 2022-10-15 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stylehub', '0012_remove_outfit_favorite_favorite_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='favorite',
            name='unique_for_question_and_user',
        ),
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(fields=('user', 'outfit'), name='unique_for_outfit_and_user'),
        ),
    ]
