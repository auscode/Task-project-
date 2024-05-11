import os
import django
import random
from faker import Faker

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskprj.settings')
django.setup()

# Import your models after Django setup
from restapp.models import Profile, SpamNumber, Contact

# Create faker instance
fake = Faker()

def populate_data():
    # Populate Profile model
    for _ in range(50):
        print("started profile")
        name = fake.name()
        phone_number = fake.phone_number()
        email = fake.email()
        password = fake.password()
        profile = Profile.objects.create(name=name, phone_number=phone_number, email=email, password=password)

        # Populate Contact model for each Profile
        for _ in range(random.randint(1, 5)):
            print("started contact")
            contact_name = fake.name()
            contact_phone_number = fake.phone_number()
            Contact.objects.create(user=profile,name=contact_name, phone_number=contact_phone_number)

    # Populate SpamNumber model
    for _ in range(20):
        print("started spam")
        number = fake.phone_number()
        SpamNumber.objects.create(number=number)

if __name__ == '__main__':
    populate_data()
    print("Data populated successfully.")
