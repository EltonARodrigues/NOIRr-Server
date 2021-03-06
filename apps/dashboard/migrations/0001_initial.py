# Generated by Django 2.1 on 2018-11-27 01:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GasesCollected',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField()),
                ('temperature', models.FloatField(default=0)),
                ('humidity', models.FloatField(default=0)),
                ('co', models.FloatField(default=0)),
                ('co2', models.FloatField(default=0)),
                ('mp25', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='gasescollected',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Sensor'),
        ),
        migrations.AlterUniqueTogether(
            name='sensor',
            unique_together={('title', 'author', 'description')},
        ),
        migrations.AlterUniqueTogether(
            name='gasescollected',
            unique_together={('created_at', 'sensor')},
        ),
    ]
