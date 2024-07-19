from django.contrib import admin
from . models import People, Contact

# Register your models here.
admin.site.register(People)

# Register your contact here
admin.site.register(Contact)