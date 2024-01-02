from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shopapp.models import Order

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create order")
        user = User.objects.get(username="valkamch")
        order = Order.objects.get_or_create(
            delivery_address="prospect Kosmonavtov, 80-24",
            promocode="SALLE0101",
            user=user,
        )


        self.stdout.write(f"Create order {order}")