from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import AboutSerializer, DocsSerializer, HandbookSerializer, WorksSerializer, LithSerializer, \
    DocsDetailSerializer, LithDetailSerializer, HandDetailBookSerializer, WorksDetailSerializer
from .models import Lithography, Works, Docs, Handbooks, About


class AboutListAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class DocListAPIView(generics.ListAPIView):
    queryset = Docs.objects.all()
    serializer_class = DocsSerializer


class DocsDetailAPIView(generics.RetrieveAPIView):
    queryset = Docs.objects.all()
    serializer_class = DocsDetailSerializer
    lookup_field = 'pk'


class HandListAPIView(generics.ListAPIView):
    queryset = Handbooks.objects.all()
    serializer_class = HandbookSerializer


class HandDetailAPIView(generics.RetrieveAPIView):
    queryset = Handbooks.objects.all()
    serializer_class = HandDetailBookSerializer
    lookup_field = 'pk'


class WorkListAPIView(generics.ListAPIView):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer


class WorkDetailAPIView(generics.RetrieveAPIView):
    queryset = Works.objects.all()
    serializer_class = WorksDetailSerializer
    lookup_field = 'pk'


class LithListAPIView(generics.ListAPIView):
    queryset = Lithography.objects.all()
    serializer_class = LithSerializer


class LithDetailAPIView(generics.RetrieveAPIView):
    queryset = Lithography.objects.all()
    serializer_class = LithDetailSerializer
    lookup_field = 'pk'


class StatisticsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        hand = Handbooks.objects.all().count()
        lith = Lithography.objects.all().count()
        doc = Docs.objects.all().count()
        total = hand + lith + doc
        return Response({'handbooks': hand, 'lithography': lith, 'docs': doc, 'total': total},
                        status=status.HTTP_200_OK)
