from djongo import models

class Team(models.Model):
    id = models.CharField(max_length=24, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = 'teams'

class User(models.Model):
    id = models.CharField(max_length=24, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=24)
    class Meta:
        db_table = 'users'

class Activity(models.Model):
    id = models.CharField(max_length=24, primary_key=True)
    user = models.CharField(max_length=24)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # minutes
    date = models.DateField()
    class Meta:
        db_table = 'activities'

class Workout(models.Model):
    id = models.CharField(max_length=24, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)
    class Meta:
        db_table = 'workouts'

class Leaderboard(models.Model):
    id = models.CharField(max_length=24, primary_key=True)
    team = models.CharField(max_length=24)
    points = models.IntegerField(default=0)
    class Meta:
        db_table = 'leaderboard'
