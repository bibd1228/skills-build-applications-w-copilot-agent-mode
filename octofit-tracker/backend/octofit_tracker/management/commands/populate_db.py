from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        try:
            # Create test users
            user1 = User.objects.create(username='john_doe', email='john@example.com', password='password123')
            user2 = User.objects.create(username='jane_doe', email='jane@example.com', password='password123')

            # Create test teams
            team1 = Team.objects.create(name='Team Alpha')
            team1.members.add(user1, user2)

            # Create test activities
            Activity.objects.create(user=user1, activity_type='Running', duration=timedelta(minutes=30))
            Activity.objects.create(user=user2, activity_type='Cycling', duration=timedelta(hours=1))

            # Create test leaderboard entries
            Leaderboard.objects.create(user=user1, score=100)
            Leaderboard.objects.create(user=user2, score=150)

            # Create test workouts
            Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session to start the day.')
            Workout.objects.create(name='HIIT', description='High-intensity interval training for fat burning.')
        except Exception as e:
            self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))