from django.contrib import admin

# Register your models here.
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published', 'price', 'list_date', 'realtor']
    list_display_links = ['title']
    list_filter = ['realtor']
    search_fields = ['title', 'description', 'address', 'city', 'state', 'price']
    
admin.site.register(Listing, ListingAdmin)