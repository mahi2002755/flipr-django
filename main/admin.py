from django.contrib import admin
from .models import Project, Client, Contact, Newsletter

admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Contact)
admin.site.register(Newsletter)

# Register your models here.
