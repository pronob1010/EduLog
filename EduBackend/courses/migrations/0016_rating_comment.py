# Generated by Django 3.0.8 on 2021-09-07 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_rating_block'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='comment',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
