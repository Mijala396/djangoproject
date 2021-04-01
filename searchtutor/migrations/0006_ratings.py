# Generated by Django 3.1.7 on 2021-03-13 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('searchtutor', '0005_sessions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutor_ratings', models.CharField(max_length=30)),
                ('tutor_review', models.CharField(max_length=30)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='searchtutor.tutor')),
            ],
        ),
    ]