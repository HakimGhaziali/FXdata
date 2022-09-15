from django.contrib import admin

# Register your models here.

from .models import Post , Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_modified',)



admin.site.register(Comment)