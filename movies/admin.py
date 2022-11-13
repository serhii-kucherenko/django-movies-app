from django.contrib import admin
from .models import Movie, Genre


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('id', 'title', 'release_year', 'number_in_stock', 'daily_rate', 'date_created')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
