from django.db import IntegrityError
from django.shortcuts import render, get_list_or_404
from rest_framework import generics, status, filters, serializers
from .models import CustomUser, ClosetItem, Outfit, Favorite
from .serializers import ClosetItemSerializer, OutfitSerializer, UserSerializer, FavoriteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.parsers import JSONParser, FileUploadParser

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
    parser_classes = [JSONParser, FileUploadParser]

    def get_parsers(self):
        if self.request.FILES:
            self.parser_classes.append(FileUploadParser)
        return [parser() for parser in self.parser_classes]
    
    


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

class FavoriteOutfitList(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = []

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user,
                            outfit=serializer.validated_data.get('outfit'))
        except IntegrityError as error:
            raise serializers.ValidationError({"error": error})


class FavoriteOutfitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = []

