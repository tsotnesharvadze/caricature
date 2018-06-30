from django.conf.urls import url
from .views import KarikaturebiRestView, set_name
urlpatterns = [
    url(r'^karikaturebi/$', KarikaturebiRestView.as_view(), name="karikaturebi"),
    url(r'^set_name/$', set_name, name="set_name")
]