from django.contrib import admin

# Register your models here.

from .models import Post , Comment , EconomicCalender

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_modified',)


admin.site.register(Comment)


@admin.register(EconomicCalender)
class EcoCal(admin.ModelAdmin):
    list_display = ('Date', 'currency','name')