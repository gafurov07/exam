from django.contrib import admin
from django.contrib.auth.models import Group, User

from apps.models import Profile


# from apps.models import Humans
# from apps.proxies import NewOrderProxy, CancelOrderProxy, CompletedOrderProxy, Order


# class BaseOrderProxyModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'product', 'user', 'quantity', 'status']
#     ordering = ['id']
#
#
# @admin.register(NewOrderProxy)
# class NewOrderProxyAdmin(BaseOrderProxyModelAdmin):
#     def get_queryset(self, request):
#         return super().get_queryset(request).filter(status=Order.Status.NEW)
#
#
# @admin.register(CancelOrderProxy)
# class CancelOrderProxyAdmin(BaseOrderProxyModelAdmin):
#     def get_queryset(self, request):
#         return super().get_queryset(request).filter(status=Order.Status.CANCEL)
#
#
# @admin.register(CompletedOrderProxy)
# class CompletedOrderProxyAdmin(BaseOrderProxyModelAdmin):
#     def get_queryset(self, request):
#         return super().get_queryset(request).filter(status=Order.Status.COMPLETED)


# @admin.register(Humans)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'username', 'website', 'wallets_balance', 'income_amounts',
#                     'total_transactions', 'image']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'description', 'image']


admin.site.unregister(Group)
admin.site.unregister(User)
