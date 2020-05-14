from django.contrib import admin
from .models import Store, Supplier, Order, Carrier

admin.site.register(Store)
admin.site.register(Supplier)
admin.site.register(Order)
admin.site.register(Carrier)
