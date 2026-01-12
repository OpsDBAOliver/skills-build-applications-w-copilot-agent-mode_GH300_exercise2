from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        # Ensure unique index on email
        db.users.create_index([('email', 1)], unique=True)

        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(id='marvel', name='Marvel')
        dc = Team.objects.create(id='dc', name='DC')

        # Create users
        users = [
            User(id='spiderman', name='Spider-Man', email='spiderman@marvel.com', team='marvel'),
            User(id='ironman', name='Iron Man', email='ironman@marvel.com', team='marvel'),
            User(id='wonderwoman', name='Wonder Woman', email='wonderwoman@dc.com', team='dc'),
            User(id='batman', name='Batman', email='batman@dc.com', team='dc'),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(id='act1', user='spiderman', type='Running', duration=30, date='2026-01-01')
        Activity.objects.create(id='act2', user='ironman', type='Cycling', duration=45, date='2026-01-02')
        Activity.objects.create(id='act3', user='wonderwoman', type='Swimming', duration=60, date='2026-01-03')
        Activity.objects.create(id='act4', user='batman', type='Yoga', duration=20, date='2026-01-04')

        # Create workouts
        Workout.objects.create(id='w1', name='Hero HIIT', description='High intensity for heroes', suggested_for='Marvel')
        Workout.objects.create(id='w2', name='Power Yoga', description='Strength and flexibility', suggested_for='DC')

        # Create leaderboard
        Leaderboard.objects.create(id='l1', team='marvel', points=100)
        Leaderboard.objects.create(id='l2', team='dc', points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
