from django.contrib import admin
from .models import UserTerm

# Register your models here.
class UserTermAdmin(admin.ModelAdmin):
    list_display = ('term', 'userId')
    search_fields = ['term']
admin.site.register(UserTerm)