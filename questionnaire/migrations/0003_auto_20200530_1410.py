# Generated by Django 3.0.5 on 2020-05-30 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_interview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question6', models.CharField(max_length=1028)),
                ('question7', models.CharField(max_length=1028)),
                ('question8', models.CharField(max_length=1028)),
                ('question9', models.CharField(max_length=1028)),
                ('question10', models.CharField(max_length=1028)),
                ('question11', models.CharField(max_length=1028)),
                ('drawing', models.CharField(max_length=1000000000)),
            ],
        ),
        migrations.RenameField(
            model_name='response',
            old_name='question1',
            new_name='question1_1',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='question2',
            new_name='question1_2',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='question3',
            new_name='question1_3',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='question4',
            new_name='question1_4',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='question5',
            new_name='question1_5',
        ),
        migrations.RemoveField(
            model_name='response',
            name='drawing',
        ),
    ]
