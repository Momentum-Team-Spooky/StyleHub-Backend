from django.shortcuts import render, get_list_or_404
from rest_framework import generics, status
from .models import CustomUser, ClosetItem, Outfit
from .serializers import ClosetItemSerializer, OutfitSerializer, UserSerializer, ClosetCompositionSerializer, OutfitEditSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .permissions import IsOwningUser
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.db import IntegrityError
from rest_framework.serializers import ValidationError
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
    filter_backends = [filters.SearchFilter]
    search_fields = ['category', 'subcategory', 'size',
                     'color', 'material', 'source', 'brand', 'tag__name']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = self.request.user.closet_items.all()
        return queryset


class MyClosetListTops(generics.ListCreateAPIView):
    serializer_class = ClosetItemSerializer
    permission_classes = [IsAuthenticated, IsOwningUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = self.request.user.closet_items.filter(category='top')
        return queryset


class MyClosetListBottoms(generics.ListCreateAPIView):
    serializer_class = ClosetItemSerializer
    permission_classes = [IsAuthenticated, IsOwningUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = self.request.user.closet_items.filter(category='bottom')
        return queryset


class MyClosetListOuterwear(generics.ListCreateAPIView):
    serializer_class = ClosetItemSerializer
    permission_classes = [IsAuthenticated, IsOwningUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = self.request.user.closet_items.filter(category='outerwear')
        return queryset


class MyClosetListShoes(generics.ListCreateAPIView):
    serializer_class = ClosetItemSerializer
    permission_classes = [IsAuthenticated, IsOwningUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = self.request.user.closet_items.filter(category='shoes')
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
    queryset = Outfit.objects.all()
    permission_classes = [IsAuthenticated, IsOwningUser]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OutfitSerializer
        elif self.request.method == 'POST':
            return OutfitEditSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = self.request.user.outfits.all()
        return queryset

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            error_data = {
                "error": "Unique constraint violation: A draft outfit has already been created."
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)


class MyDraftOutfit(generics.ListCreateAPIView):
    queryset = Outfit.objects.all()
    serializer_class = OutfitEditSerializer
    permission_classes = [IsAuthenticated, IsOwningUser]

    def get_queryset(self):
        queryset = self.request.user.outfits.filter(draft=True)
        return queryset


class OutfitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outfit.objects.all()
    permission_classes = [IsAuthenticated, IsOwningUser]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OutfitSerializer
        elif self.request.method == 'PATCH':
            return OutfitEditSerializer
        elif self.request.method == 'DELETE':
            return OutfitEditSerializer


class OutfitDetailEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outfit.objects.all()
    serializer_class = OutfitEditSerializer
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
    permission_classes = [IsAuthenticated, IsOwningUser]
    queryset = ClosetItem.objects.all()

    def get(self, request, format=None):
        queryset = self.request.user.outfits.all()
        serializer = ClosetCompositionSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
