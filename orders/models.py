from django.db import models
class customerorder(models.Model):
    starters=models.TextField()
    lunch=models.TextField()
    beverages=models.TextField()
