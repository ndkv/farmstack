from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from models import Gewaspercelen2016

class Gewaspercelen2016Serializer(HyperlinkedModelSerializer):
    class Meta:
        model = Gewaspercelen2016
        fields = ('id', 'cat_gewasc', 'gws_gewas', 'geom')

class GewaspercelenGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Gewaspercelen2016
        geo_field = 'geom'
        fields = ('id', 'cat_gewasc', 'gws_gewas', 'geom')