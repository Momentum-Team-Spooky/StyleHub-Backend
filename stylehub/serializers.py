from rest_framework import serializers
from .models import ClosetItem, Outfit, CustomUser
from rest_framework.serializers import ListSerializer
from taggit.serializers import TagListSerializerField, TaggitSerializer
from django.db.models import Count
from rest_framework.response import Response
from django.db.models import Count, F, FloatField


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
    tag = TagListSerializerField()
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    closet_item = ClosetItemSerializer(many=True, read_only=True)

    class Meta:
        model = Outfit
        fields = ('id', 'user', 'closet_item', 'title',
                  'tag', 'outfit_date', 'draft', 'favorite')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OutfitSerializer
        elif self.request.method == 'POST' | 'PATCH' | 'DELETE':
            return OutfitEditSerializer


class OutfitEditSerializer(TaggitSerializer, serializers.ModelSerializer):
    tag = TagListSerializerField()
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Outfit
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'bio', 'profile_image')


class ClosetCompositionSerializer(serializers.Serializer):
    tag = serializers.SlugRelatedField(slug_field="tag__name", read_only=True)
    color_percentages = serializers.SerializerMethodField()
    brand_percentages = serializers.SerializerMethodField()
    source_percentages = serializers.SerializerMethodField()
    category_percentages = serializers.SerializerMethodField()
    tag_percentages = serializers.SerializerMethodField()
    total_closet_items = serializers.SerializerMethodField()
    TOTAL_ITEM_COUNT = ClosetItem.objects.count()

    class Meta:
        fields = (
            'total_closet_items',
            'color_percentages',
            'brand_percentages',
            'source_percentages',
            'tag_percentages',
            'category_percentages',
        )

    def get_total_closet_items(self, obj):
        return self.TOTAL_ITEM_COUNT

    def calculate_composition(self, field):
        results = (
            ClosetItem.objects.values(field)
            .annotate(item_count=Count(field))
            .annotate(percentage=(F('item_count') * 100 / self.TOTAL_ITEM_COUNT)).order_by('-percentage')[:10]
        )
        return results

    def get_color_percentages(self, obj):
        return self.calculate_composition('color')

    def get_brand_percentages(self, obj):
        return self.calculate_composition('brand')

    def get_source_percentages(self, obj):
        return self.calculate_composition('source')

    def get_category_percentages(self, obj):
        return self.calculate_composition('category')

    def get_tag_percentages(self, obj):
        return self.calculate_composition('tag__name')
