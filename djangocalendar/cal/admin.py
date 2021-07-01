# Register your models here.
# cal/admin.py
# register it in cal/admin.py so that we can add events through the admin interface
from django.contrib import admin
from .models import Event


admin.site.register(Event)
