from django.db import models

class FrontPage(models.Model):

    topText = models.TextField()
    bottomBlockText = models.CharField(max_length=250)
    bottomImage1 = models.ImageField(upload_to='images/')
    bottomImage1Text = models.CharField(max_length=250)
    bottomImage2 = models.ImageField(upload_to='images/')
    bottomImage2Text = models.CharField(max_length=250)
    bottomImage3 = models.ImageField(upload_to='images/')
    bottomImage3Text = models.CharField(max_length=250)
    bottomImage4 = models.ImageField(upload_to='images/')
    bottomImage4Text = models.CharField(max_length=250)

    def __str__(self):
        return self.title

