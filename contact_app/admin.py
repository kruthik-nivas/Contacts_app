from django.contrib import admin
from .models import Name,PhoneNumbers,Email

# Register your models here.
admin.site.register(Name)
admin.site.register(PhoneNumbers)
admin.site.register(Email)