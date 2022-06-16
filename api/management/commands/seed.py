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
    #     'supervisor': Employee.objects.get(id=1),
    #     'position': "1st rank employee",
    #     'salary': lambda x: random.randint(350000, 600000)
    # })

    # 3750 employees -> 2nd rank
    # for _ in range(3750):
    #     emp = Employee.objects.get(id=random.randint(2, 1875))
    #     seeder.add_entity(Employee, 1, {
    #         'supervisor': emp,
    #         'position': "2nd rank employee",
    #         'salary': lambda x: random.randint(200000, 350000)
    #     })

    # 7500 employees -> 3rd rank
    # for _ in range(7500):
    #     emp = Employee.objects.get(id=random.randint(3752, 7501))
    #     seeder.add_entity(Employee, 1, {
    #         'supervisor': emp,
    #         'position': "3rd rank employee",
    #         'salary': lambda x: random.randint(150000, 200000)
    #     })

    # 15000 employees -> 4th rank
    # for _ in range(15000):
    #     emp = Employee.objects.get(id=random.randint(7502, 15001))
    #     seeder.add_entity(Employee, 1, {
    #         'supervisor': emp,
    #         'position': "4th rank employee",
    #         'salary': lambda x: random.randint(100000, 150000)
    #     })

    # 30000 employees -> 5th rank
    for _ in range(30000):
        emp = Employee.objects.get(id=random.randint(15003, 30001))
        seeder.add_entity(Employee, 1, {
            'supervisor': emp,
            'position': "5th rank employee",
            'salary': lambda x: random.randint(80000, 100000)
        })

    inserted_pks = seeder.execute()
