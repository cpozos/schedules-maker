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
        self.load_degrees()
        self.load_semester_data(args)

    def load_degrees(self):
        
        if Degree.objects.exists():
            print('Degrees already created')
            return

        degrees = [
            ('Actuaria',8),
            ('Biologáa', 8),
            ('Ciencias Ambientales',8),
            ('Ciencias de la Computación',8),
            ('Ciencias de la Tierra',8),
            ('Física',9),
            ('Física Biomédica',8),
            ('Manejo Sustentable de Zonas Costeras',8),
            ('Matemáticas', 8),
            ('Matemáticas Aplicadas', 8),
            ('Neurociencias', 8),
        ]

        for data in degrees:
            deg = Degree(name=data[0], num_periods=data[1])
            self.load_subjects_for_degree(deg.id)
            #deg.save()

    def load_subjects_for_degree(self, degree_id):
        """
        Add subjects associated to the degree to Subject table and to DegreeSubject
        If subject already exists, it skips it.
        """
        pass

    def load_semester_lessons(self, semester_id):
        semester_id = '2021-2'
        subject = ''
        professor = ''
        day = ''
