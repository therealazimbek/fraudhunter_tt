from django.core.management.base import BaseCommand
import random
from django_seed import Seed
from ...models import Employee

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'
""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def run_seed(self, mode):

    seeder = Seed.seeder()

    # 1875 employees -> 1st rank
    # seeder.add_entity(Employee, 1875, {
    #     'supervisor': Employee.objects.get(id=1)
    # })

    # 3750 employees -> 2nd rank
    # for _ in range(3750):
    #     emp = Employee.objects.get(id=random.randint(2, 1875))
    #     seeder.add_entity(Employee, 1, {
    #         'supervisor': emp
    #     })

    # 7500 employees -> 3rd rank
    # for _ in range(7500):
    #     emp = Employee.objects.get(id=random.randint(1876, 5625))
    #     seeder.add_entity(Employee, 1, {
    #         'supervisor': emp
    #     })

    # 15000 employees -> 4th rank
    # for _ in range(15000):
    #     emp = Employee.objects.get(id=random.randint(5626, 13126))
    #     seeder.add_entity(Employee, 1, {
    #         'supervisor': emp
    #     })

    # 30000 employees -> 5th rank
    # for _ in range(30000):
    #     emp = Employee.objects.get(id=random.randint(13127, 27000))
    #     seeder.add_entity(Employee, 1, {
    #         'supervisor': emp
    #     })

    inserted_pks = seeder.execute()
