from django.contrib import admin
from .models import Subject, Degree, DegreeSubject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass

class DegreeSubjectInline(admin.TabularInline):
    model = DegreeSubject

@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    inlines = [DegreeSubjectInline,]
    pass
