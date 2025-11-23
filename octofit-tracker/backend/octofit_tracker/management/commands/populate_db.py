from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Очистка данных
        Activity.objects.filter().delete()
        User.objects.filter().delete()
        Team.objects.filter().delete()
        Workout.objects.filter().delete()
        Leaderboard.objects.filter().delete()

        # Команды
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Пользователи
        users = [
            User.objects.create(name='Peter Parker', email='peter@marvel.com', team=marvel),
            User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel),
            User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc),
            User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc),
        ]

        # Активности
        Activity.objects.create(user=users[0], type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Swimming', duration=25, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Yoga', duration=60, date=timezone.now().date())

        # Тренировки
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='All')
        Workout.objects.create(name='Cardio Blast', description='30 min running', suggested_for='Marvel')
        Workout.objects.create(name='Strength', description='Weight lifting', suggested_for='DC')

        # Лидерборд
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
