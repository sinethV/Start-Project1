# Generated by Django 5.1.4 on 2025-03-13 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_branch_car_ford_person_alter_computer_image_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('studentID', models.AutoField(primary_key=True, serialize=False)),
                ('studentname', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('yearStudy', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='course.school')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('TeacherID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('schoolID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.school')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('classID', models.AutoField(primary_key=True, serialize=False)),
                ('classname', models.CharField(max_length=100)),
                ('schoolID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.school')),
                ('TeacherID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.teacher')),
            ],
        ),
    ]
