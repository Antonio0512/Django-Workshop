from django.db import models

from photos.models import Photo


class Comment(models.Model):
    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    comment_to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date_time_of_publication"]


class Like(models.Model):
    like_to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)