from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^api/talk/$', views.talk),
    ]