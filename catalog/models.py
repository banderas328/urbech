from django.db import models

class Catalog(models.Model):
    title = models.CharField(max_length=250, default='null')
    catalogText = models.TextField()
    catalogImage = models.ImageField(upload_to='images/')
    catalogGramms = models.CharField(max_length=250, default='null')
    catalogCost = models.CharField(max_length=250, default='null')

    def __str__(self):
        return self.title