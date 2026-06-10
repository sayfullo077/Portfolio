from django.contrib import admin
from .models import Experience, Project, Skill, Service


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("position", "company", "start_date", "end_date", "is_current")
    list_filter = ("is_current",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "tech_stack", "is_featured", "created_at")
    list_filter = ("is_featured",)
    search_fields = ("title", "description", "tech_stack")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "order")
    list_editable = ("level", "order")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_editable = ("order",)
