# Generated by Django 4.0.3 on 2022-04-12 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_author_name_alter_service_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.author'),
            preserve_default=False,
        ),
    ]
