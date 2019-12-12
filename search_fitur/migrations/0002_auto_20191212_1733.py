# Generated by Django 3.0 on 2019-12-12 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('search_fitur', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinfo',
            name='socmed_link',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='user_id',
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='jabatan',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='prof_pict',
            field=models.CharField(max_length=200),
        ),
    ]
