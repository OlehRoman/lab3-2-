from django.contrib import admin
from .models import Book, CustomUser, Product, Sticker

admin.site.register(Book)
admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Sticker)
