# Generated by Django 3.1.7 on 2021-03-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutor_first_name', models.CharField(max_length=30)),
                ('tutor_last_name', models.CharField(max_length=30)),
                ('tutor_username', models.CharField(max_length=30)),
                ('tutor_password', models.CharField(max_length=30)),
                ('tutor_address', models.CharField(max_length=30)),
                ('tutor_gender', models.CharField(max_length=30)),
                ('tutor_contactno', models.CharField(max_length=30)),
                ('tutor_emailaddress', models.CharField(max_length=30)),
                ('tutor_qualification', models.CharField(max_length=30)),
                ('tutor_educationalInstitute', models.CharField(max_length=30)),
                ('tutor_chargePerHour', models.CharField(max_length=30)),
            ],
        ),
    ]
