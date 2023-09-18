from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    """Details for each project"""
    title = models.CharField(max_length=255)
    brief_description = models.CharField(max_length=255, null=True)
    summary = models.TextField()
    tools_and_technologies = models.TextField(default='')
    building_process = models.TextField(default='')
    challenges = models.TextField(default='')
    improvements = models.TextField(default='')
    website_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=255, null=True)

    def __str__(self):
        return self.title
    
    def slugify_title(self):
        self.slug = slugify(self.title)

    def format_dot_points(self):
        """splits tools and technologies into separate lines so they can be rendered as dot points on the page"""
        return self.tools_and_technologies.split('\n')

    def save(self, *args, **kwargs):
        self.slugify_title()
        super().save(*args, **kwargs)


class ProjectImage(models.Model):
    """allows me to store multiple images for the same project"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')