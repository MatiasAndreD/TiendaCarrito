from django.contrib import admin
from .models import Trabajo
# Register your models here.
class TrabajosAdmin(admin.ModelAdmin):
    list_display = ("nombre","estado",)

admin.site.register(Trabajo, TrabajosAdmin)