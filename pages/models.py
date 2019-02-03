from django.db import models

class FrontPage(models.Model):
    title = models.CharField(max_length=250,default='null')
    topTextTitle = models.CharField(max_length=250,default='null')
    topText = models.TextField()
    bottomBlockText = models.CharField(max_length=250,default='null')
    bottomImage1 = models.ImageField(upload_to='images/',default='null')
    bottomImage1Text = models.CharField(max_length=250,default='null')
    bottomImage2 = models.ImageField(upload_to='images/')
    bottomImage2Text = models.CharField(max_length=250,default='null')
    bottomImage3 = models.ImageField(upload_to='images/')
    bottomImage3Text = models.CharField(max_length=250,default='null')
    bottomImage4 = models.ImageField(upload_to='images/')
    bottomImage4Text = models.CharField(max_length=250,default='null')
    topphone1 = models.CharField(max_length=250,default='null')
    topphone2 = models.CharField(max_length=250,default='null')


    def __str__(self):
        return self.title

