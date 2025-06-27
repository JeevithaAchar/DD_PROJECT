from django.contrib import admin

# Register your models here.
from ap1.models import User, History, Bin, Truck, MEmployee
admin.site.register(User)
admin.site.register(History)
admin.site.register(Bin)
admin.site.register(Truck)
admin.site.register(MEmployee)