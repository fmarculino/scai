from django.contrib import admin
from scai.registrations.models import Provider, Functionary, Requisition


class ProviderModelAdmin(admin.ModelAdmin):
    list_display = ('group', 'name', 'note')


class FunctionaryModelAdmin(admin.ModelAdmin):
    list_display = (
        'group', 'name', 'membership', 'conjugate', 'salary', 'note')


class RequisitionModelAdmin(admin.ModelAdmin):
    list_display = (
        'number', 'provider', 'requester', 'functionary', 'activity',
        'discount', 'created_at', 'note')


admin.site.register(Provider, ProviderModelAdmin)
admin.site.register(Functionary, FunctionaryModelAdmin)
admin.site.register(Requisition, RequisitionModelAdmin)
