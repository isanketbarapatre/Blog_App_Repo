from django.db import models

# Create your models here.

class blogapi(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title