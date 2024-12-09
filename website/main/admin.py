from django.contrib import admin
from .models import *


# import the Booking model

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'is_active', 'is_staff')
    list_filter = ('user_type', 'is_staff', 'is_active')

@admin.register(DriverProfile)
class DriverProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'license_number')

    # Custom queryset to show only drivers
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(user__user_type='driver')

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address')

    # Optionally customize how 'user' is displayed if needed
    def user(self, obj):
        return obj.user.username  # Display only the username for user field
    user.admin_order_field = 'user'  # Allow ordering by user field

@admin.register(CarReg)
class CarRegAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phonenumber', 'district', 'country', 'city', 'Transportation')
    search_fields = ('firstname', 'lastname', 'phonenumber', 'district', 'country', 'city')
    list_filter = ('Transportation',)

    fieldsets = (
        (None, {
             'fields': ('firstname', 'lastname', 'phonenumber', 'district', 'country', 'city', 'Transporation')
         }),
     )


from .models import Deal

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'clicked_by', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description')
