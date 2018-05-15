# Generated by Django 2.0.2 on 2018-05-12 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Time_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('task_name', models.CharField(max_length=60)),
                ('project_name', models.CharField(max_length=60)),
                ('client_name', models.CharField(max_length=40)),
                ('activity_start', models.DateTimeField()),
                ('activity_end', models.DateTimeField()),
            ],
        ),
    ]
