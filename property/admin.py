from django.contrib import admin

from .models import Flat, Claim, Owner

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'owners_phonenumber',  'town', 'town_district', 'address',)
    readonly_fields = ['created_at']
    list_display = ('owner', 'owners_phonenumber','address', 'price','new_building','construction_year','town',)
    list_editable = ['new_building']
    list_filter = ('new_building','rooms_number','has_balcony',)
    raw_id_fields = ('liked_by',)


class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('author','flat',)

class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('owner','owner_pure_phone',)
    list_display = ('owner', 'owner_pure_phone',)
    raw_id_fields = ('owner_flat',)

admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Owner, OwnerAdmin)



