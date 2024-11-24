from django.contrib import admin
from service.models import todo
# Register your models here.

class TODO(admin.ModelAdmin):
    pass

admin.site.register(todo,TODO)
    
