from rest_framework import serializers
from .models import ClosetItem, Outfit
from rest_framework.serializers import ListSerializer
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class ClosetItemSerializer(TaggitSerializer, serializers.ModelSerializer):

    tag = TagListSerializerField()

    class Meta:
        model = ClosetItem
        fields = "__all__"
