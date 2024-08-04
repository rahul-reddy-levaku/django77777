from django.contrib import admin
from testapp.models import FilterModel
class FilterModeAdmin(admin.ModelAdmin):
    list_display = ['name','subject','dept','date']
admin.site.register(FilterModel,FilterModeAdmin)

# Register your models here.
