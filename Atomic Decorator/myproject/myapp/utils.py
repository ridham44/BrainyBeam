from django.db import transaction
from django.db.utils import IntegrityError
from myapp.models import MyModel

@transaction.atomic
def save_data(data):
    try:
        obj = MyModel(**data)
        obj.save()
        print("Data saved successfully!")
    except IntegrityError as e:
        print(f"Error saving data: {e}")
