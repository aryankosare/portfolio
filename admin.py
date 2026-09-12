from django.contrib import admin
from .models import Portfolio, Project, Skill


class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'slug', 'updated_at')
    prepopulated_fields = {'slug': ('full_name',)}
    inlines = [ProjectInline, SkillInline]
