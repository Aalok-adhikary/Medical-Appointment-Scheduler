from django.contrib import admin
from .models import Appointment
from .models import Doctor
admin.site.register(Appointment)

admin.site.register(Doctor)