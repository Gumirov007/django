from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="videos/thumbnail")
    source = models.FileField(upload_to='videos')

    def __str__(self):
        return f"{self.id} - {self.title}"
