# Generated by Django 5.1.7 on 2025-03-23 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_attribute_attributevalue_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productattribute',
            old_name='attribute_key_id',
            new_name='attribute_key',
        ),
        migrations.RenameField(
            model_name='productattribute',
            old_name='attribute_value_id',
            new_name='attribute_value',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
