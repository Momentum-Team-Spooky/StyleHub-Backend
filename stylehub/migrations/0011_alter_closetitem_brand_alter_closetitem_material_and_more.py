# Generated by Django 4.0 on 2022-10-14 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stylehub', '0010_alter_closetitem_color_alter_closetitem_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closetitem',
            name='brand',
            field=models.CharField(blank=True, default='unknown', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='closetitem',
            name='material',
            field=models.CharField(blank=True, default='unknown', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='closetitem',
            name='size',
            field=models.CharField(blank=True, default='unknown', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='closetitem',
            name='source',
            field=models.CharField(blank=True, choices=[('brand_store', 'Brand Store'), ('department_store', 'Department Store'), ('discount_store', 'Discount Store'), ('thrift_shop', 'Thrift Shop'), ('resale/consignment_shop', 'Resale/Consignment Shop'), ('friend', 'Friend'), ('other', 'Other')], default='unknown', max_length=50, null=True),
        ),
    ]