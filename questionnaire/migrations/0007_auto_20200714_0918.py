# Generated by Django 3.0.5 on 2020-07-14 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0006_auto_20200624_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview_q',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(max_length=1028)),
                ('question2', models.CharField(max_length=1028)),
            ],
        ),
        migrations.AddField(
            model_name='interview',
            name='name',
            field=models.CharField(default=1, max_length=1028),
            preserve_default=False,
        ),
    ]
