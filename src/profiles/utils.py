import random
import string
from django.conf import settings


SHORTCODE_MIN = getattr(settings,"SHORTCODE_MIN", 35)


def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    # new code = ''
    # for _ in range(size):
    #   new_code += random.choice(chars)
    # return new_code
    return ''.join(random.choice(chars) for _ in range(size))
