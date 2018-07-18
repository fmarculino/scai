from django.contrib import admin
from easy_select2 import select2_modelform
from scai.registrations.models import Provider, Functionary, Requisition


class ProviderModelAdmin(admin.ModelAdmin):
    list_display = ('group', 'name', 'note')


class FunctionaryModelAdmin(admin.ModelAdmin):
    list_display = (
        'group', 'name', 'membership', 'conjugate', 'salary', 'note')


RequisitionForm = select2_modelform(Requisition, attrs={'width': '250px'})

class RequisitionModelAdmin(admin.ModelAdmin):
    form = select2_modelform(Requisition)

    list_display = (
        'number', 'provider', 'requester', 'functionary', 'activity',
        'discount', 'created_at', 'note')


admin.site.register(Provider, ProviderModelAdmin)
admin.site.register(Functionary, FunctionaryModelAdmin)
admin.site.register(Requisition, RequisitionModelAdmin)
