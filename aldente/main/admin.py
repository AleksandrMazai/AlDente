from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CategoryPortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Contact)
admin.site.register(Portfolio)
admin.site.register(CategoryPortfolio, CategoryPortfolioAdmin)
