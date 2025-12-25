from django.db import models # type: ignore
from django.contrib.auth.models import User # type:ignore
from froala_editor.fields import FroalaField  # type:ignore
from .helper import *



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)

    

class BlogModel(models.Model):
    title=models.CharField(max_length=500)
    user=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    content= FroalaField()
    slug=models.SlugField(max_length=600, null=True , blank=True)
    image=models.ImageField(upload_to='Blog')
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.title)
            
        super(BlogModel, self).save(*args, **kwargs)