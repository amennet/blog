from django.contrib import admin

# Register your models here.

from django.contrib import admin
from blogpost.models import Blogpost

class BlogpostAdmin(admin.ModelAdmin):
#    exclude = ['posted']
    list_display = ('title', 'posted')
#    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blogpost, BlogpostAdmin)
