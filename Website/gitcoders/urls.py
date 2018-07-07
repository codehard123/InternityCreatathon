
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^',include('votes.urls')),
    url(r'^location-map$',TemplateView.as_view(template_name="map.html"), name='location_map'),
    url(r'^admin/', admin.site.urls),
]
