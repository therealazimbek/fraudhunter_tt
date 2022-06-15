from django_seed import Seed
from models import Employee

seeder = Seed.seeder()

seeder.add_entity(Employee, 1870, {
    'supervisor': 1
})

inserted_pks = seeder.execute()
