from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(id='testteam', name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(id='testteam', name='Test Team')
        user = User.objects.create(id='testuser', name='Test User', email='test@example.com', team='testteam')
        self.assertEqual(user.email, 'test@example.com')

    def test_activity_creation(self):
        team = Team.objects.create(id='testteam', name='Test Team')
        user = User.objects.create(id='testuser', name='Test User', email='test@example.com', team='testteam')
        activity = Activity.objects.create(id='testactivity', user='testuser', type='Running', duration=10, date='2026-01-01')
        self.assertEqual(activity.type, 'Running')

    def test_workout_creation(self):
        workout = Workout.objects.create(id='testworkout', name='Test Workout', description='Desc', suggested_for='Test')
        self.assertEqual(workout.name, 'Test Workout')

    def test_leaderboard_creation(self):
        team = Team.objects.create(id='testteam', name='Test Team')
        leaderboard = Leaderboard.objects.create(id='testlb', team='testteam', points=50)
        self.assertEqual(leaderboard.points, 50)
