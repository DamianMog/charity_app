from django.core.management.base import BaseCommand
from core.models import Category, Institution, Donation
from account.models import NewUser
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Fill the db'

    def handle(self, *args, **options):
        before_c_user = NewUser.objects.all().count()
        before_c_ins = Institution.objects.all().count()
        before_c_cat = Category.objects.all().count()
        before_c_don = Donation.objects.all().count()

        fake = Faker(['pl_PL'])
        for _ in range(15):
            x = fake.first_name()
            NewUser.objects.create_user(first_name=x, password=x,
                                        email=fake.ascii_company_email())
        for _ in range(random.randint(10, 20)):
            cat = Category.objects.create(name=fake.word())
            cat.save()

        for _ in range(random.randint(5, 15)):
            ins = Institution.objects.create(name=fake.domain_name(),
                                             description=fake.text(max_nb_chars=80),
                                             type=random.randint(1, 3))
            ins.save()
            for _ in range(random.randint(3, 6)):
                cat = Category.objects.all().order_by('?')[0]
                ins.categories.add(cat)

        for _ in range(random.randint(80, 100)):
            user = NewUser.objects.all().order_by('?')[0]
            ins = Institution.objects.all().order_by('?')[0]
            cat = Category.objects.all().order_by('?')[0]
            d = Donation.objects.create(quantity=random.randint(1, 50),
                                        institution=ins,
                                        address=fake.street_address(),
                                        phone_number=random.randint(222222222, 999999999),
                                        city=fake.city(),
                                        zip_code=fake.postcode(),
                                        pick_up_date=fake.date(),
                                        pick_up_time=random.randint(0, 1449),
                                        pick_up_comment=fake.text(max_nb_chars=40),
                                        user=user)
            d.save()
            d.categories.add(cat)

        after_c_user = NewUser.objects.all().count()
        after_c_ins = Institution.objects.all().count()
        after_c_cat = Category.objects.all().count()
        after_c_don = Donation.objects.all().count()

        self.stdout.write(self.style.SUCCESS('Wypełnienie bazy pomyślne:'))
        self.stdout.write(self.style.SUCCESS(f'User: {before_c_user} -> {after_c_user}'))
        self.stdout.write(self.style.SUCCESS(f'Institution: {before_c_ins} -> {after_c_ins}'))
        self.stdout.write(self.style.SUCCESS(f'Category: {before_c_cat} -> {after_c_cat}'))
        self.stdout.write(self.style.SUCCESS(f'Donation: {before_c_don} -> {after_c_don}'))
