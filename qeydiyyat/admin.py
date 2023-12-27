from django.contrib import admin
from .models import AdminQeydiyyatForm, AdminSinaqQeydiyyatForm, AdminElaqeForm

class IstedadQeydiyyatForm(admin.ModelAdmin):
    list_display = ("fname", "lname", "telNo_basliq", "telNo", "rayon", "mekteb", "sinif", "blok", "xdil")

class IstedadSinaqQeydiyyatForm(admin.ModelAdmin):
    list_display = ("fname", "lname", "telNo_basliq", "telNo", "rayon", "mekteb", "sinif", "blok", "xdil")

class IstedadElaqeForm(admin.ModelAdmin):
    list_display = ("fname", "lname",)

admin.site.register(AdminQeydiyyatForm, IstedadQeydiyyatForm)
admin.site.register(AdminSinaqQeydiyyatForm, IstedadSinaqQeydiyyatForm)
admin.site.register(AdminElaqeForm, IstedadElaqeForm)