# Generated by Django 3.0.6 on 2020-05-28 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200527_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='sailstudent',
            name='dietary_restrictions',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='sailstudent',
            name='gender_identification',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Non_Binary', 'Non-binary')], default='Male', max_length=10),
        ),
        migrations.AddField(
            model_name='sailstudent',
            name='high_school',
            field=models.CharField(default='noschool', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sailstudent',
            name='home_city',
            field=models.CharField(default='nocity', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sailstudent',
            name='home_state',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='sailstudent',
            name='home_zip_code',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sailstudent',
            name='parent_email',
            field=models.EmailField(default='nopemail@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sailstudent',
            name='parent_name',
            field=models.CharField(default='nopname', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sailstudent',
            name='parent_phone_number',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sailstudent',
            name='phone_number',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sailstudent',
            name='shirt_size',
            field=models.CharField(choices=[('XS', 'Unisex XS'), ('S', 'Unisex S'), ('M', 'Unisex M'), ('L', 'Unisex L'), ('XL', 'Unisex XL')], default='XS', max_length=5),
        ),
        migrations.AlterField(
            model_name='sailstudent',
            name='admitted_student',
            field=models.BooleanField(blank=True),
        ),
    ]
