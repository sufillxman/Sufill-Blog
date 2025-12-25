from django.utils.text import slugify 
import random
import string

def generate_random_string(n):
   
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=n))
    return random_string


def generate_slug(text):
    new_slug = slugify(text)
    from Home.models import BlogModel
    if BlogModel.objects.filter(slug=new_slug).exists():
        return generate_slug(text + ' ' + generate_random_string(5))
    return new_slug