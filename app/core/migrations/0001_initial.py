# Generated by Django 4.0.7 on 2022-09-11 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('country', models.CharField(max_length=50)),
                ('league', models.CharField(max_length=50)),
                ('fixture', models.CharField(max_length=50)),
                ('home_win', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('away_win', models.IntegerField()),
                ('home_form', models.IntegerField()),
                ('away_form', models.IntegerField()),
            ],
            options={
                'ordering': ['date', '-home_win', '-away_win'],
            },
        ),
    ]
