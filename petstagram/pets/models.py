from django.db import models
from django.template.defaultfilters import slugify


class Pet(models.Model):
    pet_name = models.CharField(max_length=30)
    pet_photo = models.URLField()
    pet_birth = models.DateField(blank=True, null=True)
    pet_slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.pet_slug:
            self.pet_slug = slugify(f"{self.pet_name}-{self.id}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.pet_name