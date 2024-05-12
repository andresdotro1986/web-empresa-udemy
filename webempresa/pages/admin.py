from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

    list_display=('title','order')
    # Sirve para acomodar el orden de los campos en el admin,primero hay que crear "orden" en models.py
admin.site.register(Page,PageAdmin)
