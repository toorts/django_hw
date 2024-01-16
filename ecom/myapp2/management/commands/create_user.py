from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        # user = User(name='John', email='john@example.com', phone_number='79995554444', address='Elm Street')
        # user = User(name='Neo', email='neo@example.com', phone_number='79995555555', address='Fargo Ave')
        user = User(name='Jack', email='jack@example.com', phone_number='79995558888', address='Redemption Street')
        user.save()
        self.stdout.write(f'{user}')