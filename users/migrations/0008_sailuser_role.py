# Generated by Django 3.0.6 on 2020-05-29 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200528_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='sailuser',
            name='role',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student')], max_length=10, null=True),
        ),
    ]
