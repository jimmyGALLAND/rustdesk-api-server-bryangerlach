# Generated by Django 5.0.3 on 2024-04-06 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_rustdesdevice_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rustdesdevice',
            options={'ordering': ('-rid',), 'verbose_name': 'Device', 'verbose_name_plural': 'Device List'},
        ),
        migrations.AlterModelOptions(
            name='rustdeskpeer',
            options={'ordering': ('-username',), 'verbose_name': 'Peers', 'verbose_name_plural': 'Peers List'},
        ),
        migrations.AlterModelOptions(
            name='rustdesktag',
            options={'ordering': ('-uid',), 'verbose_name': 'Tags', 'verbose_name_plural': 'Tags List'},
        ),
        migrations.AlterModelOptions(
            name='rustdesktoken',
            options={'ordering': ('-username',), 'verbose_name': 'Token', 'verbose_name_plural': 'Token List'},
        ),
        migrations.AlterModelOptions(
            name='sharelink',
            options={'ordering': ('-create_time',), 'verbose_name': 'Share Link', 'verbose_name_plural': 'Link List'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('view_task', 'Can see available tasks'), ('change_task_status', 'Can change the status of tasks'), ('close_task', 'Can remove a task by setting its status as closed')), 'verbose_name': 'User', 'verbose_name_plural': 'User List'},
        ),
        migrations.AddField(
            model_name='rustdesdevice',
            name='ip',
            field=models.CharField(default='', max_length=16, verbose_name='IP Address'),
        ),
        migrations.AddField(
            model_name='rustdeskpeer',
            name='ip',
            field=models.CharField(default='', max_length=16, verbose_name='IP Address'),
        ),
        migrations.AlterField(
            model_name='rustdesdevice',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Device Registration Time'),
        ),
        migrations.AlterField(
            model_name='rustdesdevice',
            name='hostname',
            field=models.CharField(max_length=100, verbose_name='Hostname'),
        ),
        migrations.AlterField(
            model_name='rustdesdevice',
            name='memory',
            field=models.CharField(max_length=100, verbose_name='Memory'),
        ),
        migrations.AlterField(
            model_name='rustdesdevice',
            name='os',
            field=models.CharField(max_length=100, verbose_name='Operating System'),
        ),
        migrations.AlterField(
            model_name='rustdesdevice',
            name='rid',
            field=models.CharField(blank=True, max_length=60, verbose_name='Client ID'),
        ),
        migrations.AlterField(
            model_name='rustdesdevice',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='设备更新时间'),
        ),
        migrations.AlterField(
            model_name='rustdesdevice',
            name='username',
            field=models.CharField(blank=True, max_length=100, verbose_name='System Username'),
        ),
        migrations.AlterField(
            model_name='rustdesdevice',
            name='version',
            field=models.CharField(max_length=100, verbose_name='Client Version'),
        ),
        migrations.AlterField(
            model_name='rustdeskpeer',
            name='alias',
            field=models.CharField(max_length=30, verbose_name='Alias'),
        ),
        migrations.AlterField(
            model_name='rustdeskpeer',
            name='hostname',
            field=models.CharField(max_length=30, verbose_name='Operating System Name'),
        ),
        migrations.AlterField(
            model_name='rustdeskpeer',
            name='platform',
            field=models.CharField(max_length=30, verbose_name='Platform'),
        ),
        migrations.AlterField(
            model_name='rustdeskpeer',
            name='rhash',
            field=models.CharField(max_length=60, verbose_name='Device Connection Password'),
        ),
        migrations.AlterField(
            model_name='rustdeskpeer',
            name='rid',
            field=models.CharField(max_length=60, verbose_name='Client ID'),
        ),
        migrations.AlterField(
            model_name='rustdeskpeer',
            name='tags',
            field=models.CharField(max_length=30, verbose_name='Tag'),
        ),
        migrations.AlterField(
            model_name='rustdeskpeer',
            name='uid',
            field=models.CharField(max_length=16, verbose_name='User ID'),
        ),
        migrations.AlterField(
            model_name='rustdeskpeer',
            name='username',
            field=models.CharField(max_length=20, verbose_name='System Username'),
        ),
        migrations.AlterField(
            model_name='rustdesktag',
            name='tag_color',
            field=models.CharField(blank=True, max_length=60, verbose_name='Tag Color'),
        ),
        migrations.AlterField(
            model_name='rustdesktag',
            name='tag_name',
            field=models.CharField(max_length=60, verbose_name='Tag Name'),
        ),
        migrations.AlterField(
            model_name='rustdesktag',
            name='uid',
            field=models.CharField(max_length=16, verbose_name='Belongs to User ID'),
        ),
        migrations.AlterField(
            model_name='rustdesktoken',
            name='access_token',
            field=models.CharField(blank=True, max_length=60, verbose_name='Access Token'),
        ),
        migrations.AlterField(
            model_name='rustdesktoken',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Login Time'),
        ),
        migrations.AlterField(
            model_name='rustdesktoken',
            name='uid',
            field=models.CharField(max_length=16, verbose_name='User ID'),
        ),
        migrations.AlterField(
            model_name='rustdesktoken',
            name='username',
            field=models.CharField(max_length=20, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='rustdesktoken',
            name='uuid',
            field=models.CharField(max_length=60, verbose_name='UUID'),
        ),
        migrations.AlterField(
            model_name='sharelink',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Generation Time'),
        ),
        migrations.AlterField(
            model_name='sharelink',
            name='is_expired',
            field=models.BooleanField(default=False, verbose_name='Is Expired'),
        ),
        migrations.AlterField(
            model_name='sharelink',
            name='is_used',
            field=models.BooleanField(default=False, verbose_name='Is Used'),
        ),
        migrations.AlterField(
            model_name='sharelink',
            name='peers',
            field=models.CharField(max_length=20, verbose_name='Machine ID List'),
        ),
        migrations.AlterField(
            model_name='sharelink',
            name='shash',
            field=models.CharField(max_length=60, verbose_name='Link Key'),
        ),
        migrations.AlterField(
            model_name='sharelink',
            name='uid',
            field=models.CharField(max_length=16, verbose_name='User ID'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='deviceInfo',
            field=models.TextField(blank=True, verbose_name='Login Information:'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Is Administrator'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=50, unique=True, verbose_name='Username'),
        ),
    ]
