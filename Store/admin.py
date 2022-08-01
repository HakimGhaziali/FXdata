from django.contrib import admin

# Register your models here.


from .models import Book

class Display(admin.ModelAdmin):

    list_display = ['title','author']



admin.site.register(Book,Display)