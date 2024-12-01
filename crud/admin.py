from django.contrib import admin
from .models import authors, books

admin.site.register(authors)
admin.site.register(books)
