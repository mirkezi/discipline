from django.contrib import admin

from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    '''django admin page -> settings for disciplineapp/users page'''
    list_display = ['username','password','is_active']
    list_filter = ['is_active']
    search_fields = ['username']


#register both User model and UserAdmin admin model to the admin page.
admin.site.register(User, UserAdmin)