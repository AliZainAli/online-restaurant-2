from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.IntegerField(blank=True)
    address = models.CharField(max_length=500, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Category(models.Model):
    category_title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_title


class Order(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders')
    address = models.CharField(max_length=500, default=None)


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    details = models.CharField(max_length=1000)
    price = models.IntegerField()
    item_logo = models.FileField()
    category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.PROTECT,related_name="orderItems", null=True, blank=True)

    def __str__(self):
        return self.name


class ItemInline(admin.TabularInline):
    model = Item


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline,
    ]
