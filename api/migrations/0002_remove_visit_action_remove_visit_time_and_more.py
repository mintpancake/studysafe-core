# Generated by Django 4.0.3 on 2022-04-13 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='action',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='time',
        ),
        migrations.AddField(
            model_name='visit',
            name='enter_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='exit_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='status',
            field=models.CharField(choices=[('S', 'Stay'), ('L', 'Leave')], default='L', max_length=1),
        ),
    ]