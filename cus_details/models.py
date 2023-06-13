from django.db import models
class customer(models.Model):
    name=models.TextField(max_length=20)
    phone=models.TextField(max_length=10)
    gmail=models.TextField()
    tableno=models.PositiveIntegerField()