# Generated by Django 3.0.3 on 2020-02-05 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cricket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Match Date/Time')),
                ('venue', models.CharField(max_length=50, verbose_name='Venue')),
                ('match_format', models.CharField(choices=[('t20', 'T-20'), ('odi', 'ODI'), ('test', 'Test')], max_length=15, verbose_name='Format')),
                ('tournament_name', models.CharField(max_length=80, verbose_name='Tournament Name')),
                ('team1', models.CharField(max_length=50, verbose_name='Team 1')),
                ('team2', models.CharField(max_length=50, verbose_name='Team 2')),
            ],
            options={
                'verbose_name': 'Cricket',
                'verbose_name_plural': 'Crickets',
            },
        ),
        migrations.CreateModel(
            name='CricketPlayerT20',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('photo', models.ImageField(upload_to=None, verbose_name='Photo')),
                ('player_type', models.CharField(choices=[('batsman', 'Batsman'), ('allrounder', 'All-Rounder'), ('wicketkeeper', 'Wicket Keeper'), ('baller', 'Baller')], max_length=15, verbose_name='Player Type')),
                ('matches', models.IntegerField(blank=True, null=True, verbose_name='Matches')),
                ('innings', models.IntegerField(blank=True, null=True, verbose_name='Innings')),
                ('batting_style', models.CharField(blank=True, choices=[('right_handed', 'Right-Handed'), ('left_handed', 'Right-Handed')], max_length=50, null=True, verbose_name='Batting Style')),
                ('career_runs', models.IntegerField(blank=True, null=True, verbose_name='Career Runs')),
                ('catches', models.IntegerField(blank=True, null=True, verbose_name='Catches')),
                ('bat_average', models.FloatField(blank=True, null=True, verbose_name='Batting Average')),
                ('wickets', models.IntegerField(blank=True, null=True, verbose_name='Wickets')),
                ('balling_style', models.CharField(blank=True, choices=[('right_handed', 'Right-Handed'), ('left_handed', 'Right-Handed')], max_length=50, null=True, verbose_name='Balling Style')),
                ('ball_average', models.FloatField(blank=True, null=True, verbose_name='Ball Average')),
                ('highest_score', models.SmallIntegerField(blank=True, null=True, verbose_name='Highest Score')),
                ('hightest_wicket', models.SmallIntegerField(blank=True, null=True, verbose_name='Highest Wicket')),
                ('fifties', models.SmallIntegerField(blank=True, null=True, verbose_name='50s')),
                ('hundreds', models.SmallIntegerField(blank=True, null=True, verbose_name='100s')),
            ],
            options={
                'verbose_name': 'Cricket Player T-20',
                'verbose_name_plural': 'Cricket Players T-20',
            },
        ),
        migrations.CreateModel(
            name='CricketPlayerIPL',
            fields=[
                ('cricketplayert20_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sports.CricketPlayerT20')),
            ],
            options={
                'verbose_name': 'Cricket Player IPL',
                'verbose_name_plural': 'Cricket Players IPL',
            },
            bases=('sports.cricketplayert20',),
        ),
        migrations.CreateModel(
            name='CricketPlayerODI',
            fields=[
                ('cricketplayert20_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sports.CricketPlayerT20')),
            ],
            options={
                'verbose_name': 'Cricket Player ODI',
                'verbose_name_plural': 'Cricket Players ODI',
            },
            bases=('sports.cricketplayert20',),
        ),
        migrations.CreateModel(
            name='CricketPlayerTest',
            fields=[
                ('cricketplayert20_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sports.CricketPlayerT20')),
            ],
            options={
                'verbose_name': 'Cricket Player Test',
                'verbose_name_plural': 'Cricket Players Test',
            },
            bases=('sports.cricketplayert20',),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Team Name')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports.Cricket', verbose_name='Tournament')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.AddField(
            model_name='cricketplayert20',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports.Team', verbose_name='Team'),
        ),
    ]
