from django.contrib import admin

from movies.models import Movie, People, Category

admin.site.register(Movie)
admin.site.register(People)
admin.site.register(Category)
