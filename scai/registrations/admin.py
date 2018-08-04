from django.contrib import admin
from django.utils.html import format_html
from easy_select2 import select2_modelform
from scai.registrations.models import Provider, Functionary, Requisition

RequisitionForm = select2_modelform(Requisition, attrs={'width': '250px'})


class ProviderModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'note')
    search_fields = ('name',)
    list_filter = ('group',)


class FunctionaryModelAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'membership', 'conjugate', 'group', 'salary', 'note')
    search_fields = ('name', 'membership', 'conjugate')
    list_filter = ('salary', 'group')


class RequisitionModelAdmin(admin.ModelAdmin):
    form = select2_modelform(Requisition)
    list_display = (
        'number', 'provider', 'requester', 'functionary', 'activity',
        'value', 'note', 'documento', 'created_at')
    search_fields = ('number', 'provider', 'requester', 'functionary')
    list_filter = ('provider', 'requester', 'functionary', 'created_at')

    def documento(self, instance):
        return format_html("<a href='{url}' target='_blank'>URL</a>", url=instance.document_url)


admin.site.register(Provider, ProviderModelAdmin)
admin.site.register(Functionary, FunctionaryModelAdmin)
admin.site.register(Requisition, RequisitionModelAdmin)
