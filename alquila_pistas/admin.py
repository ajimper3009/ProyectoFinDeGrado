from django.contrib import admin

from .models import *

admin.site.register(UserProfile)
admin.site.register(Court)
admin.site.register(Reservation)
admin.site.register(Group)
