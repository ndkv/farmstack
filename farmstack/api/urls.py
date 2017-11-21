from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
import views

API_TITLE = 'FarmStack API'
API_DESCRIPTION = 'Friendly open data agri powered by AgroDataCube'

router = routers.DefaultRouter()
router.register(r'gewaspercelen', views.Gewaspercelen2016ViewSet, 'gewaspercelen')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]