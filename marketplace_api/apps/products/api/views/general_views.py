from rest_framework import generics
from rest_framework import viewsets

from apps.base.api import GeneralListApiView
from apps.products.models import MeasureUnit, Indicator, CategoryProduct
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer

class MeasureUnitViewSet(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

class IndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

class CategoryProductViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
