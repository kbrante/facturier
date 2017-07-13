from django.core.management.base import BaseCommand
from factures.models import *
from django.core.mail import send_mail
from django.utils import timezone
import pytz

class Command(BaseCommand):
    def handle(self, *args, **options):
        propositions = Proposition.objects.all()
        waiting = Status.objects.get(id=2)
        pending = Status.objects.get(id=5)
        now = timezone.now()
        now_1_month = now.replace(month = now.month-1)

        for proposition in propositions:
            if proposition.status == waiting :
                date_proposal = proposition.date_creation
                if date_proposal <= now_1_month:

                    send_mail(
                                    'relance',
                                    'payez nous.',
                                    'from@example.com',
                                    ['to@example.com'],
                                    fail_silently=False,
                                        )
            elif proposition.status == pending:
                darte_proposal = proposition.date_creation
                if darte_proposal <= now_1_month:

                    send_mail(
                                    'bijour',
                                    'ou etes vous ? ',
                                    'from@example.com',
                                    ['to@example.com'],
                                    fail_silently=False,
                                        )
