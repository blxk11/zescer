from django.contrib import admin

# Register your models here.
from .models import User, Jobs, Application

admin.site.register(User)
admin.site.register(Jobs)
admin.site.register(Application)