from django.core.management.base import BaseCommand
import csv,sqlite3

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('export_facturier.csv','rb')as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')
            csvreader.next()
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
