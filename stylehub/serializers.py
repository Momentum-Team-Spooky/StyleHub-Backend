from rest_framework import serializers
from .models import ClosetItem, Outfit, CustomUser, GenericStringTaggedClosetItem, GenericStringTaggedOutfit
from rest_framework.serializers import ListSerializer
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)



class ClosetItemSerializer(TaggitSerializer, serializers.ModelSerializer):
    tag = TagListSerializerField()
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    user_id = serializers.SerializerMethodField()
    item_image = serializers.ImageField(read_only=True)

    class Meta:
        model = ClosetItem
        fields = ('id', 'item_choice', 'size', 'color', 'material', 'brand', 'source', 'tag', 'item_image', 'added_at', 'user_id', 'user'
                  )
        read_only_fields = ['item_image']

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
    closet_item = ClosetItemSerializer(many=True, read_only=True)
    outfit_image = serializers.ImageField(read_only=True)

    class Meta:
        model = Outfit
        fields = "__all__"
        read_only_field = ["outfit_image"]


class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'bio', 'profile_image')
        read_only_field = ["profile_image"]
