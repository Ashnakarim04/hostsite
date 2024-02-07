import pandas as pd
from django.core.management.base import BaseCommand
from website.models import Student

class Command(BaseCommand):
    help = 'Bulk create students from an Excel sheet'

    def handle(self, *args, **kwargs):
        excel_file_path = 'D:\\SEM 9\\students_database.xlsx'
  # Update with the correct path

        # Load data from Excel
        df = pd.read_excel(excel_file_path)

        # Iterate through the rows and create student objects
        for index, row in df.iterrows():
            username = row['username']
            password = row['password']

            # Create student (Django will automatically assign an 'id')
            Student.objects.create(username=username, password=password)

        self.stdout.write(self.style.SUCCESS('Students created successfully.'))
