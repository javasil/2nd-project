# Generated by Django 4.0.3 on 2022-04-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('sub_title', models.CharField(max_length=120)),
                ('link', models.URLField(max_length=190)),
            ],
        ),
    ]
