# Generated by Django 2.2 on 2019-05-10 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0004_auto_20190510_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='imgs',
            field=models.ImageField(null=True, upload_to='hotpic'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='price',
            field=models.IntegerField(default=45, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='rate',
            field=models.IntegerField(null=True, verbose_name='评级'),
        ),
    ]