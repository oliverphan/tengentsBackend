from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'', include('chatbot.urls')),
]
