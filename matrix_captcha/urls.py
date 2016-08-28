from django.conf.urls import include, url
from django.contrib import admin

from ticket.views import ticket_service_view

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ticket-service/$', ticket_service_view),
]
