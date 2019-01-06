from django.db import models

class Catalog(models.Model):
    catalogTitle = models.CharField(max_length=250)
    catalogText = models.TextField()
    catalogImage = models.ImageField(upload_to='images/')
    catalogGramms = models.CharField(max_length=250)
    catalogCost = models.CharField(max_length=250)

    def __str__(self):
        return self.title