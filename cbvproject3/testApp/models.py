from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=128)
    location=models.CharField(max_length=64)
    Ceo=models.CharField(max_length=230)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
