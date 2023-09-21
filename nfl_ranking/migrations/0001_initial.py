# Generated by Django 4.2.5 on 2023-09-21 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NFLGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.CharField(max_length=20)),
                ('week', models.IntegerField()),
                ('home_team', models.CharField(max_length=3)),
                ('away_team', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Turnover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turnover_type', models.CharField(max_length=20)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nfl_ranking.nflgame')),
            ],
        ),
    ]