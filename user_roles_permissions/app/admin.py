from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Permission)
