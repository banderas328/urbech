from django.db import models

class Recipes(models.Model):
    title = models.CharField(max_length=250)
    recipesText = models.TextField()
    recipesImage = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title