from django.db import models
from django.core.validators import MinValueValidator

class UserCount(models.Model):
    image_to_pdf = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0)])
    word_to_pdf = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0)])
