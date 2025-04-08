from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email='test@example.com', name='Test User', age=20)
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Team A', members=['user1', 'user2'])
        self.assertEqual(team.name, 'Team A')

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        activity = Activity.objects.create(user='user1', type='running', duration=30, date='2025-04-08')
        self.assertEqual(activity.type, 'running')

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(user='user1', points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups', duration=10)
        self.assertEqual(workout.name, 'Pushups')