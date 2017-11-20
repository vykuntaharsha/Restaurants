from django.core.exceptions import ValidationError


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )


CATEGORIES = ['Mexican', 'American', 'Indian', 'Italian']


def validate_category(value):

    if value.capitalize() not in CATEGORIES:
        raise ValidationError(f"{value} is not a valid category")
