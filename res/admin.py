from django.contrib import admin
from .models import Profile, Category, Item , Order , CategoryAdmin


admin.site.register(Profile)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order)
admin.site.register(Item)