# Generated by Django 2.2.6 on 2019-11-13 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191113_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review_file',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d/filtered'),
        ),
        migrations.AlterField(
            model_name='store',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d/filtered'),
        ),
        migrations.AlterField(
            model_name='store_file',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d/filtered'),
        ),
    ]