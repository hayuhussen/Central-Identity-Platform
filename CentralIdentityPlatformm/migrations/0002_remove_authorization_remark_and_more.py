# Generated by Django 4.2.7 on 2024-04-01 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CentralIdentityPlatformm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorization',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='governmentagency',
            name='state',
        ),
        migrations.RemoveField(
            model_name='service',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='userauthenticationlog',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='userexperience',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='usergovernmentagency',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='userserviceaccess',
            name='remark',
        ),
        migrations.AddField(
            model_name='authorization',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Inactive')], default=1),
        ),
        migrations.AddField(
            model_name='identityprovider',
            name='status',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Inactive')], default=1),
        ),
        migrations.AddField(
            model_name='userauthenticationlog',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Inactive')], default=1),
        ),
        migrations.AddField(
            model_name='userexperience',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Inactive')], default=1),
        ),
        migrations.AddField(
            model_name='userserviceaccess',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Inactive')], default=1),
        ),
        migrations.AlterField(
            model_name='governmentagency',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='governmentagency',
            name='status',
            field=models.CharField(default='Active', max_length=20),
        ),
    ]