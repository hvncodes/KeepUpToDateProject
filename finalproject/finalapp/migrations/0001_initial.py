# Generated by Django 2.1.5 on 2019-03-13 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=255)),
                ('evententrydate', models.DateField()),
                ('producturl', models.URLField(blank=True, null=True)),
                ('eventdescription', models.TextField()),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=255)),
                ('typedescription', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'eventtype',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='eventtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finalapp.EventType'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
