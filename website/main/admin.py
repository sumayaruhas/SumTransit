from django.contrib import admin
from .models import *
from .models import Deal, DealStatus
from .models import Booking


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

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at', 'image']

@admin.register(DealStatus)
class DealStatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'deal', 'status']



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'pickup_location', 'dropoff_location', 'status')
    list_filter = ('status',)
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(status='approved')  # Update the 'status' field
        self.message_user(request, "Selected bookings have been approved.")  # Optional success message

    approve_bookings.short_description = "Approve selected bookings"
