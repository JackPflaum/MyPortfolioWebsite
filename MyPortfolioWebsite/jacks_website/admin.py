from django.contrib import admin
from .models import Project

#decorator directly registers model class Project with ProjectAdmin without calling admin.site.register() function separately.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass