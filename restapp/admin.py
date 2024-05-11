from django.contrib import admin
from .models import Profile, SpamNumber, Contact

# Register your models here.

admin.site.register(Profile)
admin.site.register(SpamNumber)
admin.site.register(Contact)