"""scai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.utils.translation import ugettext_lazy as _

from scai.core.views import DocumentRequisitionView

#     path('admin/', admin.site.urls),
urlpatterns = [
    path('', admin.site.urls),
    path('requisitions/<int:pk>/document', DocumentRequisitionView.as_view(), name='document-requisition')
]

# Change admin site title
admin.site.site_header = _("Administração Porekro-Admin")
admin.site.site_title = _("Scai - Porekro")

