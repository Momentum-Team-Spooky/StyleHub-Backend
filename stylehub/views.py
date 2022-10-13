from django.shortcuts import render, get_list_or_404
from rest_framework import generics, status
from .models import CustomUser, ClosetItem, Outfit
from .serializers import ClosetItemSerializer, OutfitSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'mycloset/': reverse('my-closet-items', request=request, format=format),
        'myoutfits/': reverse('my-outfits', request=request, format=format),
    })


class MyClosetList(generics.ListCreateAPIView):
    serializer_class = ClosetItemSerializer
    permission_classes = []

    def get_queryset(self):
        queryset = self.request.user.closet_items.all()
        return queryset


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClosetItem.objects.all()
    serializer_class = ClosetItemSerializer
    permission_classes = []


class MyOutfitList(generics.ListCreateAPIView):
    serializer_class = OutfitSerializer
    permission_classes = []

    def get_queryset(self):
        queryset = self.request.user.outfits.all()
        return queryset


class OutfitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outfit.objects.all()
    serializer_class = OutfitSerializer
    permission_classes = []


class UserProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    def get_object(self):
        return self.request.user


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
