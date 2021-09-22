# Generated by Django 3.0.8 on 2021-09-22 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_auto_20210922_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='testchoice',
            name='Course',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
        migrations.AddField(
            model_name='testchoice',
            name='Lesson',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson'),
        ),
    ]
