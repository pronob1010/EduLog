# Generated by Django 3.2.7 on 2021-09-03 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=50)),
                ('course_description', models.TextField(blank=True, max_length=150, null=True)),
                ('course_price', models.PositiveIntegerField()),
                ('course_discount_price', models.PositiveIntegerField()),
                ('activate', models.BooleanField(default=False)),
                ('thumbnail', models.ImageField(upload_to='Course/Thumbnail')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('materials_link', models.URLField(blank=True, null=True)),
                ('course_length', models.CharField(blank=True, max_length=15, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseBaseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Base_Category_Title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lesson_Title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('Course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='WillLearn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(max_length=50)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video_Title', models.CharField(max_length=50)),
                ('Video_URL', models.URLField()),
                ('is_Preview', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('Course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('Lesson', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='courses.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=100)),
                ('option_1', models.CharField(max_length=50)),
                ('option_2', models.CharField(max_length=50)),
                ('option_3', models.CharField(max_length=50)),
                ('option_4', models.CharField(max_length=50)),
                ('Correct_Answer', models.CharField(max_length=50)),
                ('Time_In_Secound', models.PositiveIntegerField()),
                ('Course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('Lesson', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='courses.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Prerequisite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(max_length=50)),
                ('Course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tags_Title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('Course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='Course_Base_Category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='courses.coursebasecategory'),
        ),
    ]
