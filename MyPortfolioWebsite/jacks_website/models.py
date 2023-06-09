from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    title = models.CharField(max_length=255)
    brief_description = models.CharField(max_length=255, null=True)
    details = models.TextField()
    website_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='images/projects/')
    slug = models.SlugField(unique=True, max_length=255, null=True)

    def __str__(self):
        return self.title
    
    def slugify_title(self):
        self.slug = slugify(self.title)

    def save(self, *args, **kwargs):
        self.slugify_title()
        super().save(*args, **kwargs)
