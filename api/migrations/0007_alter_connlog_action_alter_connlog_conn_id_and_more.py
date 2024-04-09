# Generated by Django 5.0.3 on 2024-04-09 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_connlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connlog',
            name='action',
            field=models.CharField(max_length=20, null=True, verbose_name='Action'),
        ),
        migrations.AlterField(
            model_name='connlog',
            name='conn_id',
            field=models.IntegerField(null=True, verbose_name='Connection ID'),
        ),
        migrations.AlterField(
            model_name='connlog',
            name='from_ip',
            field=models.CharField(max_length=30, null=True, verbose_name='From IP'),
        ),
        migrations.AlterField(
            model_name='connlog',
            name='logged_at',
            field=models.CharField(max_length=25, null=True, verbose_name='Logged At'),
        ),
        migrations.AlterField(
            model_name='connlog',
            name='rid',
            field=models.CharField(max_length=20, null=True, verbose_name='To ID'),
        ),
        migrations.AlterField(
            model_name='connlog',
            name='session_id',
            field=models.IntegerField(null=True, verbose_name='Session ID'),
        ),
        migrations.AlterField(
            model_name='connlog',
            name='uuid',
            field=models.CharField(max_length=60, null=True, verbose_name='UUID'),
        ),
    ]
