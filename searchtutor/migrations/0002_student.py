# Generated by Django 3.1.7 on 2021-03-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchtutor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_first_name', models.CharField(max_length=30)),
                ('student_last_name', models.CharField(max_length=30)),
                ('student_username', models.CharField(max_length=30)),
                ('student_password', models.CharField(max_length=30)),
                ('student_address', models.CharField(max_length=30)),
                ('student_gender', models.CharField(max_length=30)),
                ('student_contactno', models.CharField(max_length=30)),
                ('student_emailaddress', models.CharField(max_length=30)),
                ('student_academicLevel', models.CharField(max_length=30)),
            ],
        ),
    ]
