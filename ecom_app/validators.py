from django.core.exceptions import ValidationError

def validate_acceptable_categories(title):
    categories = ['house','outdoors','professional']
    if title not in categories:
        raise ValidationError("This category does not exist!")