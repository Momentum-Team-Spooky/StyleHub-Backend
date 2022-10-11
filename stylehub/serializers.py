from rest_framework import serializers
from .models import ClosetItem, Outfit
from rest_framework.serializers import ListSerializer


class ClosetItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClosetItem
        fields = "__all__"
