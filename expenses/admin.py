from django.contrib import admin

# Register your models here.
from .models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['category', 'amount', 'description', 'owner','date']


admin.site.register(Expense, ExpenseAdmin)