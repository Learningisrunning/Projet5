# Generated by Django 4.1.7 on 2023-03-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0004_alter_demandercritiquemod_img_livre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creercritiquemod',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='demandercritiquemod',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
