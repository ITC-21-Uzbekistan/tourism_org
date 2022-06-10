from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db import transaction

from .models import Country
from .pagination import CountryPagination
from .serializers import CountrySerializerForAll, CountrySerializerForAdmin, CountryCreateSerializerForAdmin


class ListCountryViewForAll(ListAPIView):
    queryset = Country.objects.filter(id_delete=False)
    serializer_class = CountrySerializerForAll
    permission_classes = (AllowAny,)
    pagination_class = CountryPagination
    filter_backends = (SearchFilter,)

    def list(self, request, *args, **kwargs):
        lang = request.headers.get('lang', 'en')

        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(self.queryset, many=True, context={'lang': lang})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True, context={'lang': lang})
        return Response(serializer.data, status=HTTP_200_OK)


class RetrieveCountryViewForAll(RetrieveAPIView):
    queryset = Country.objects.filter(is_delete=False)
    serializer_class = CountrySerializerForAll
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        lang = request.headers.get('lang', 'en')

        serializer = self.get_serializer(self.get_object(), context={'lang': lang})
        return Response(serializer.data, status=HTTP_200_OK)


class ListCountryViewForAdmin(ListCreateAPIView):
    queryset = Country.objects.filter(is_delete=False)
    serializer_class = CountrySerializerForAdmin
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)

    def list(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = CountryCreateSerializerForAdmin(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=HTTP_201_CREATED)


class RetrieveUpdateDestroyCountryViewForAdmin(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.filter(is_delete=False)
    serializer_class = CountrySerializerForAdmin
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)