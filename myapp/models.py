from django.db import models

# Create your models here.
# models.py
from django.db import models

class files_mod(models.Model):
    images = models.FileField(upload_to='files/')
