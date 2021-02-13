from django.core.management import BaseCommand
from api.models import Degree

#https://stackoverflow.com/questions/56008730/how-to-debug-django-custom-management-command-using-vs-code
class Command(BaseCommand):
    # Show this when the user types help
    help = "Updates the data from the page"


    def add_arguments(self, parser):

        # Optional parameters
        parser.add_argument(
            '--f', 
            type=bool, 
            help='force to update')

    def handle(self, *args, **options):

        force = options['f']
        print(args)
        return


        self.load_degrees()
        self.load_semester_data(args)

    def load_degrees(self):
        
        if Degree.objects.exists():
            print('Degrees already created')
            return

        degrees = [
            ('Física',9)
            ('Matematicas', 8)
            ('Biologia', 8)
            ('Ciencias de la computacion',8)
            ('Ciencias de la tierra',8)
            ('Actuaria',8)
        ]

        for data in degrees:
            deg = Degree(name=data[0], num_periods=data[1])
            deg.save()

    def load_semester_data(self, *args):
        name = '2021-2'






