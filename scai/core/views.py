from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from scai.registrations.models import Requisition


class DocumentRequisitionView(LoginRequiredMixin, DetailView):
    template_name = 'core/requisition.html'
    queryset = Requisition.objects.all()
    context_object_name = 'requisition'

