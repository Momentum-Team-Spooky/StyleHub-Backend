from django.shortcuts import render, get_list_or_404
from rest_framework import generics, status
from .models import CustomUser, ClosetItem, Outfit
from .serializers import ClosetItemSerializer, OutfitSerializer, UserSerializer, ClosetCompositionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .permissions import IsOwningUser
from rest_framework import filters
from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.views import APIView
# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'mycloset/': reverse('my-closet-items', request=request, format=format),
        'myoutfits/': reverse('my-outfits', request=request, format=format),
    })


class MyClosetList(generics.ListCreateAPIView):
    serializer_class = ClosetItemSerializer
    permission_classes = [IsAuthenticated, IsOwningUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = self.request.user.closet_items.all()
        return queryset


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClosetItem.objects.all()
    serializer_class = ClosetItemSerializer
    permission_classes = [IsAuthenticated, IsOwningUser]
    parser_classes = [JSONParser, FileUploadParser]

    def get_parsers(self):
        if self.request.FILES:
            self.parser_classes.append(FileUploadParser)
        return [parser() for parser in self.parser_classes]


class MyOutfitList(generics.ListCreateAPIView):
    serializer_class = OutfitSerializer
    permission_classes = [IsAuthenticated, IsOwningUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = self.request.user.outfits.all()
        return queryset


class OutfitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outfit.objects.all()
    serializer_class = OutfitSerializer
    permission_classes = [IsAuthenticated, IsOwningUser]


class UserProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwningUser]

    def get_object(self):
        return self.request.user


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class FavoriteOutfitsList(generics.ListAPIView):
    queryset = Outfit.objects.filter(favorite=True)
    serializer_class = OutfitSerializer
    permission_classes = [IsAuthenticated, IsOwningUser]

    def get_queryset(self):
        queryset = self.request.user.outfits.filter(favorite=True)
        return queryset


class ClosetComposition(APIView):

    def get(self, request, format=None):
        queryset = ClosetItem.objects.all()
        serializer = ClosetCompositionSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class ColorComposition(generics.ListAPIView):

#     def get(self, request, format=None):
#         total_count = ClosetItem.objects.count()
#         color_qs = ClosetItem.objects.values('color').annotate(
#             Count('color')).order_by('-color__count')[:10]

#         composition = {}

#         for colors in color_qs:
#             percent = colors['color__count'] / total_count * 100
#             colors['percent'] = percent
#         composition['colors'] = color_qs
#         return Response(composition)


# class SourceComposition(generics.ListAPIView):

#     def get(self, request, format=None):
#         total_count = ClosetItem.objects.count()
#         composition = {}

#         source_qs = ClosetItem.objects.values(
#             'source').annotate(Count('source')).order_by('-source__count')

#         for sources in source_qs:
#             percent = sources['source__count'] / total_count * 100
#             sources['percent'] = percent
#         composition['source'] = source_qs
#         return Response(composition)


# class BrandComposition(generics.ListAPIView):

#     def get(self, request, format=None):
#         total_count = ClosetItem.objects.count()
#         composition = {}

#         brand_qs = ClosetItem.objects.values(
#             'brand').annotate(Count('brand')).order_by('-brand__count')

#         for brands in brand_qs:
#             percent = brands['brand__count'] / total_count * 100
#             brands['percent'] = percent
#         composition['brand'] = brand_qs
#         return Response(composition)


# class TagComposition(generics.ListAPIView):

#     def get(self, request, format=None):
#         total_count = ClosetItem.objects.count()
#         composition = {}

#         tag_qs = ClosetItem.objects.values(
#             'tag').annotate(Count('tag')).order_by('-tag_count')

#         for tags in tag_qs:
#             percent = tags['tag__count'] / total_count * 100
#             tags['percent'] = percent
#         composition['tag'] = tag_qs
#         return Response(composition)

    # category_qs = ClosetItem.objects.values(
    #     'category').annotate(Count('category')).order_by('-category__count')[:10]
