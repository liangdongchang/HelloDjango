# Generated by Django 3.2.11 on 2022-01-23 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=10)),
                ('gdate', models.DateTimeField()),
                ('ggirlnum', models.IntegerField()),
                ('gboynum', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('sgender', models.BooleanField(default=True)),
                ('sage', models.IntegerField()),
                ('sinfo', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
                ('sgrade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.grade')),
            ],
        ),
    ]
