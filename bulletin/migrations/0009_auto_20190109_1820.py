# Generated by Django 2.1.3 on 2019-01-09 22:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0008_auto_20190108_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationTeller',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('secret', models.CharField(max_length=100)),
                ('registration_public_key', models.CharField(max_length=250)),
                ('registration_private_key_hash', models.CharField(max_length=250)),
                ('secret_key', models.CharField(max_length=250)),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulletin.Election')),
            ],
        ),
        migrations.DeleteModel(
            name='Registrar',
        ),
    ]
