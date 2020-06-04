from django.contrib import admin
from .models import Course
# Register your models here.

class course_admin(admin.ModelAdmin):
    list_display = ['nome', 'atalho', 'data_de_inicio', 'criado']
    search_fields = ['nome']
    prepopulated_fields = {'atalho':('nome',)}

admin.site.register(Course, course_admin)