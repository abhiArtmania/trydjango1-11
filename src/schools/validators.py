from django.core.exceptions import ValidationError

def validate_name(value):
    if value.capitalize() == 'Name':
        raise ValidationError("Name is not allowed in Name field")

ALLOWED_LOCATIONS = ['Varanasi','Delhi','Noida','Mirzapur']

def validate_location(value):
    cat = value.capitalize()
    if not cat in ALLOWED_LOCATIONS:
        raise ValidationError(f"{value} location is not allowed")
