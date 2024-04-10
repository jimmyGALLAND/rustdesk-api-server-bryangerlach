# Generated by Django 5.0.3 on 2024-04-10 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_connlog_conn_end_alter_connlog_conn_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rustdeskpeer',
            name='hostname',
            field=models.CharField(blank=True, max_length=30, verbose_name='Operating System Name'),
        ),
        migrations.AlterField(
            model_name='rustdeskpeer',
            name='ip',
            field=models.CharField(blank=True, default='', max_length=16, verbose_name='IP Address'),
        ),
        migrations.AlterField(
            model_name='rustdeskpeer',
            name='platform',
            field=models.CharField(blank=True, max_length=30, verbose_name='Platform'),
        ),
        migrations.AlterField(
            model_name='rustdeskpeer',
            name='rhash',
            field=models.CharField(blank=True, max_length=60, verbose_name='Device Connection Password'),
        ),
        migrations.AlterField(
            model_name='rustdeskpeer',
            name='tags',
            field=models.CharField(blank=True, max_length=30, verbose_name='Tag'),
        ),
        migrations.AlterField(
            model_name='rustdeskpeer',
            name='username',
            field=models.CharField(blank=True, max_length=20, verbose_name='System Username'),
        ),
    ]
