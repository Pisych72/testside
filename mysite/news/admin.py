from django.contrib import admin
from .models import *
# Register your models here.

class newsAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','created_at','updated_at','is_published','photo')
    list_display_links = ('id','title',)
    search_fields = ('title','content','created_at')
    list_editable = ('is_published','category',)
    list_filter = ('is_published','category',)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','title',)
    list_display_links = ('id','title',)
    search_fields = ('title',)

admin.site.register(news,newsAdmin)
admin.site.register(Category,categoryAdmin)