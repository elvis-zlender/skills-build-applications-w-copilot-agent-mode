from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users (super heroes)
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create Activities
        activities = [
            Activity(user=users[0], type='Running', duration=30),
            Activity(user=users[1], type='Cycling', duration=45),
            Activity(user=users[2], type='Swimming', duration=60),
            Activity(user=users[3], type='Yoga', duration=40),
        ]
        for activity in activities:
            activity.save()

        # Create Workouts
        workouts = [
            Workout(name='Morning Cardio', description='Cardio workout for all'),
            Workout(name='Strength Training', description='Strength workout for all'),
        ]
        for workout in workouts:
            workout.save()

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=90)
        Leaderboard.objects.create(user=users[2], score=95)
        Leaderboard.objects.create(user=users[3], score=85)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
