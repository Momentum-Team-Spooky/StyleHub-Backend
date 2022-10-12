from rest_framework import serializers
from .models import ClosetItem, Outfit
from rest_framework.serializers import ListSerializer
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class ClosetItemSerializer(TaggitSerializer, serializers.ModelSerializer):
    tag = TagListSerializerField()
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    user_id = serializers.SerializerMethodField()

    class Meta:
        model = ClosetItem
        fields = ('id', 'item_choice', 'size', 'color', 'material', 'brand', 'source', 'tag', 'item_image', 'added_at', 'user_id', 'user'
                  )

    def get_user_id(self, obj):
        return obj.user.id


class OutfitSerializer(TaggitSerializer, serializers.ModelSerializer):
    tag = TagListSerializerField
    closet_item = ClosetItemSerializer(many=True, read_only=True)

    class Meta:
        model = Outfit
        fields = "__all__"
