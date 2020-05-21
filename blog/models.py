from django.db import models

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=130)
    author = models.CharField(max_length=20)
    content = models.TextField()
    slug = models.CharField(max_length=130)
    timestamp = models.DateTimeField(blank=True)
    def __str__(self):
        return self.title + ' by ' + self.author
    class meta:
        ordering=['-timestamp']