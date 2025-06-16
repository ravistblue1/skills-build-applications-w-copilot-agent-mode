from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        User.objects.create(email='user1@example.com', name='User One', password='password1')
        User.objects.create(email='user2@example.com', name='User Two', password='password2')

        # Create test teams
        Team.objects.create(name='Team Alpha', members=['User One', 'User Two'])

        # Create test activities
        Activity.objects.create(user=User.objects.get(email='user1@example.com'), type='Running', duration=30)
        Activity.objects.create(user=User.objects.get(email='user2@example.com'), type='Cycling', duration=45)

        # Create test leaderboard
        Leaderboard.objects.create(team=Team.objects.get(name='Team Alpha'), score=100)

        # Create test workouts
        Workout.objects.create(user=User.objects.get(email='user1@example.com'), description='Morning Yoga', date='2025-06-16')
        Workout.objects.create(user=User.objects.get(email='user2@example.com'), description='Evening Cardio', date='2025-06-16')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
