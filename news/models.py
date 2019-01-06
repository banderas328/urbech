from django.db import models

class News(models.Model):
    newsTitle = models.CharField(max_length=250)
    newsText = models.TextField()
    newsImage = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
