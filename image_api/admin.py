from django.contrib import admin
from .models import record
# Register your models here.

class recordAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name', 'species', 'weight', 'length', 'latitude', 'longitude', 'timestamp', 'image']
    list_display = [field.name for field in record._meta.get_fields()]

admin.site.register(record, recordAdmin)
