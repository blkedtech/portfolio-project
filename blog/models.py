from django.db import models

# Create your models here.

# Create a Blog models
class Blog(models.Model):
    # title
    title = models.CharField(max_length=255)
    # pub_date
    pub_date = models.DateTimeField()
    # body
    body = models.TextField()
    # image
    image = models.ImageField(upload_to='images/')

# Add the Blog to the "settings": ('blog.apps.BlogConfig',)

# Create a migration: (> python manage.py makemigration)

# Migrate: (> python manage.py migrate)

# Add to the "admin": (from .models import Blog) (admin.site.register(Blog)
