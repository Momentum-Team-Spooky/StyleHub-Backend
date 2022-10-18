from rest_framework import serializers
from .models import ClosetItem, Outfit, CustomUser
from rest_framework.serializers import ListSerializer
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from django.db.models import Count
from rest_framework.response import Response


class ClosetItemSerializer(TaggitSerializer, serializers.ModelSerializer):
    tag = TagListSerializerField()
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    user_id = serializers.SerializerMethodField()
    item_image = serializers.ImageField()

    class Meta:
        model = ClosetItem
        fields = ('id', 'category', 'subcategory', 'size', 'color', 'material',
                  'brand', 'source', 'tag', 'item_image', 'added_at', 'user_id', 'user')

    def get_user_id(self, obj):
        return obj.user.id

    def update(self, instance, validated_data):

        if "file" in self.initial_data:
            file = self.initial_data.get("file")
            instance.item_image.save(file.name, file, save=True)
            return instance
        # this call to super is to make sure that update still works for other fields
        return super().update(instance, validated_data)


class OutfitSerializer(TaggitSerializer, serializers.ModelSerializer):
    tag = TagListSerializerField
    # closet_item = ClosetItemSerializer(many=True, read_only=True)

    class Meta:
        model = Outfit
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'bio', 'profile_image')


# class ClosetCompSerializer(TaggitSerializer, serializers.ModelSerializer):
#     tag = TagListSerializerField()

#     class Meta:
#         model = ClosetItem
#         fields = ('category', 'subcategory', 'color', 'brand', 'source', 'tag')

#     @property
#     def get_color(self, request, format=None):
#         total_count = ClosetItem.objects.count()
#         composition = {}

#         source_qs = ClosetItem.objects.values(
#             'source').annotate(Count('source')).order_by('-source__count')

#         for sources in source_qs:
#             percent = sources['source__count'] / total_count * 100
#             sources['percent'] = percent
#         composition['source'] = source_qs
#         return Response(composition)
