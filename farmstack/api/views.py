# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, mixins
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

    # def bbox_filter(self, bbox):
    #     bbox_geom = 'POLYGON (({}))'.format(bbox.replace(',', ' '))
    #
    #     return Gewaspercelen2016.objects.filter(geom__contained=bbox_geom)

    def get_queryset(self):
        point = self.request.query_params.get('point', None)
        bbox = self.request.query_params.get('bbox', None)

        if point is not None:
            return self.point_filter(point)

        # if bbox is not None:
        #     return self.bbox_filter(bbox)

        return Gewaspercelen2016.objects.all()
