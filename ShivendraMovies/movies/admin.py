from django.contrib import admin
from movies.models import Movie

# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    list_display=['rdate','Moviename','Hero','Heroine','Rating']
admin.site.register(Movie,MoviesAdmin)
