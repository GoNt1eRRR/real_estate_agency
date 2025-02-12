from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = ['owner']


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']
    list_display = ['user', 'flat', 'text']


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    inlines = [OwnerInline]
    search_fields = ["town", "address"]
    readonly_fields = ["created_at"]
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ['likes']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phonenumber', 'pure_phone']
    search_fields = ['name', 'phonenumber']
    raw_id_fields = ['flat']

