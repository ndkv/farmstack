from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from main.views import index as api_index

urlpatterns = [
    url(r'^$', api_index),
    url(r'^api/v1/', include('api.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)