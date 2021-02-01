from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    story = models.TextField()
    date = models.DateField()
    #author

    def __str__(self):
        return self.title

