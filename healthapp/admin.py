from django.contrib import admin

from healthapp.models import Patient,Myappointment


# Register your models here.

admin.site.register(Patient)
admin.site.register(Myappointment)

