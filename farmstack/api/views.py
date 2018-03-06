# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, mixins
from django.contrib.gis.geos import Point, Polygon
from serializers import Gewaspercelen2016Serializer, GewaspercelenGeoSerializer

from models import Gewaspercelen2016

class Gewaspercelen2016ViewSet(mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               viewsets.GenericViewSet):
    queryset = Gewaspercelen2016.objects.all()
    # serializer_class = Gewaspercelen2016Serializer
    serializer_class = GewaspercelenGeoSerializer

    def point_filter(self, point):
        x, y = point.split(',')
        return Gewaspercelen2016.objects.filter(geom__contains='POINT({} {})'.format(x, y))

    def bbox_filter(self, bbox):
        bbox_geom = Polygon.from_bbox(bbox.split(','))

        return Gewaspercelen2016.objects.filter(geom__intersects=bbox_geom)

    def get_queryset(self):
        point = self.request.query_params.get('point', None)
        bbox = self.request.query_params.get('bbox', None)

        if point:
            return self.point_filter(point)

        if bbox:
            return self.bbox_filter(bbox)

        return Gewaspercelen2016.objects.all()
