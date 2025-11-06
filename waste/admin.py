from django.contrib import admin
from .models import WasteCategory, WasteRequest, CollectionSchedule

@admin.register(WasteCategory)
class WasteCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(WasteRequest)
class WasteRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'status', 'created_at', 'scheduled_date']
    list_filter = ['status', 'category', 'created_at']
    search_fields = ['user__username', 'address']
    list_editable = ['status', 'scheduled_date']
    date_hierarchy = 'created_at'

@admin.register(CollectionSchedule)
class CollectionScheduleAdmin(admin.ModelAdmin):
    list_display = ['area', 'day_of_week', 'time_slot']
    filter_horizontal = ['waste_types']