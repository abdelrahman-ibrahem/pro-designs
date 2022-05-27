from django.contrib import admin
from .models import Contact

class CustomizeContact(admin.ModelAdmin):
    list_display = ['name' , 'email' , 'phone' , 'message' , 'created_at']
    list_filter = ['name' , 'created_at']

admin.site.register(Contact , CustomizeContact)
