from django.core.management.base import BaseCommand
import csv
from factures.models import *
from datetime import datetime
import pytz

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('export_facturier.csv','rb')as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')
            csvreader.next()
            projet = None
            date_up = None
            for row in csvreader:
                id, customer, status, creation_date, update_date, product, price, qty = row
                print id,\
                        customer,\
                        status,\
                        creation_date,\
                        update_date,\
                        product,\
                        price,\
                        qty

                if status == "STANDBY" and id[0] == "D":
                    statut = Status.objects.get(id=5)
                elif status == "STANDBY" and id[0] == "F":
                    statut = Status.objects.get(id=2)
                elif status == "LOST":
                    statut = Status.objects.get(id=4)
                elif status == "PAID":
                    statut = Status.objects.get(id=3)
                if update_date != '':
                    date_up = pytz.utc.localize(datetime.strptime(update_date, '%d/%m/%y %H:%M'))
                if id != projet :

                    proposition = Proposition.objects.create(
                        dealer = User.objects.get(id=2),
                        customer = Profile.objects.get(id=3),
                        status = statut,
                        proposition = id,
                        date_creation = pytz.utc.localize(datetime.strptime(creation_date, '%d/%m/%y %H:%M')),
                        date_update = date_up
                    )

                Ligne.objects.create(
                    service_name = product,
                    unit_price = price,
                    quantity = qty,
                    proposal = proposition
                )

                projet = id
