# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 12:57
from __future__ import unicode_literals

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
            name='AbstractStandingsRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactID', models.IntegerField()),
                ('contactType', models.IntegerField()),
                ('requestDate', models.DateTimeField(auto_now_add=True)),
                ('actionDate', models.DateTimeField(null=True)),
                ('effective', models.BooleanField(default=False)),
                ('effectiveDate', models.DateTimeField(null=True)),
            ],
            options={
                'permissions': (('affect_standings', 'User can process standings requests.'), ('request_standings', 'User can request standings.')),
            },
        ),
        migrations.CreateModel(
            name='AllianceStanding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactID', models.IntegerField()),
                ('name', models.CharField(max_length=254)),
                ('standing', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CharacterAssociation',
            fields=[
                ('character_id', models.IntegerField(primary_key=True, serialize=False)),
                ('corporation_id', models.IntegerField(null=True)),
                ('alliance_id', models.IntegerField(null=True)),
                ('main_character_id', models.IntegerField(null=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labelID', models.IntegerField()),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ContactSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=254)),
            ],
            options={
                'permissions': (('view', 'User can view standings'), ('download', 'User can export standings to a CSV file')),
                'get_latest_by': 'date',
            },
        ),
        migrations.CreateModel(
            name='CorpStanding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactID', models.IntegerField()),
                ('name', models.CharField(max_length=254)),
                ('standing', models.FloatField()),
                ('labels', models.ManyToManyField(to='standingsrequests.ContactLabel')),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='standingsrequests.ContactSet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EveNameCache',
            fields=[
                ('entityID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=254)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PilotStanding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactID', models.IntegerField()),
                ('name', models.CharField(max_length=254)),
                ('standing', models.FloatField()),
                ('inWatchlist', models.BooleanField(default=False)),
                ('labels', models.ManyToManyField(to='standingsrequests.ContactLabel')),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='standingsrequests.ContactSet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StandingsRequest',
            fields=[
                ('abstractstandingsrequest_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='standingsrequests.AbstractStandingsRequest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('standingsrequests.abstractstandingsrequest',),
        ),
        migrations.CreateModel(
            name='StandingsRevocation',
            fields=[
                ('abstractstandingsrequest_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='standingsrequests.AbstractStandingsRequest')),
            ],
            bases=('standingsrequests.abstractstandingsrequest',),
        ),
        migrations.AddField(
            model_name='contactlabel',
            name='set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='standingsrequests.ContactSet'),
        ),
        migrations.AddField(
            model_name='alliancestanding',
            name='labels',
            field=models.ManyToManyField(to='standingsrequests.ContactLabel'),
        ),
        migrations.AddField(
            model_name='alliancestanding',
            name='set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='standingsrequests.ContactSet'),
        ),
        migrations.AddField(
            model_name='abstractstandingsrequest',
            name='actionBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
