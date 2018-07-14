from django.contrib import admin
from scai.registrations.models import Providers, Functionarys, Requisitions


class ProvidersModelAdmin(admin.ModelAdmin):
    list_display = ('group', 'name', 'note')


class FunctionarysModelAdmin(admin.ModelAdmin):
    list_display = (
        'group', 'name', 'membership', 'conjugate', 'salary', 'note')


class RequisitionsModelAdmin(admin.ModelAdmin):
    list_display = (
        'number', 'provider', 'requester', 'functionary', 'activity',
        'discount', 'created_at', 'note')


admin.site.register(Providers, ProvidersModelAdmin)
admin.site.register(Functionarys, FunctionarysModelAdmin)
admin.site.register(Requisitions, RequisitionsModelAdmin)
