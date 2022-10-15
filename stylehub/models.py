from django.contrib.auth.models import AbstractUser
from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import CommonGenericTaggedItemBase, TaggedItemBase
# Create your models here.


class CustomUser(AbstractUser):
    bio = models.TextField(
        max_length=1000,
        null=True,
        blank=True)
    profile_image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True)

    def __str__(self):
        return self.username

class GenericStringTaggedClosetItem(CommonGenericTaggedItemBase, TaggedItemBase):
    object_id = models.CharField(max_length=50, verbose_name=_('Object id'), db_index=True)

class GenericStringTaggedOutfit(CommonGenericTaggedItemBase, TaggedItemBase):
    object_id = models.CharField(max_length=50, verbose_name=_('Object id'), db_index=True)

class TaggedClosetItem(TaggedItemBase):
       closet_items = models.ForeignKey('ClosetItem', on_delete=models.CASCADE)

class TaggedOutfit(TaggedItemBase):
       closet_items = models.ForeignKey('Outfit', on_delete=models.CASCADE)

class ClosetItem(models.Model):
    ITEM_CHOICES = [
        ('Top', (
            ('button-down', 'Button-down'),
            ('dress', 'Dress'),
            ('shirt', 'Shirt'),
            ('sweater', 'Sweater'),
            ('t-shirt', 'T-shirt'),
        )
        ),
        ('Bottom', (
            ('pants', 'Pants'),
            ('shorts', 'Shorts'),
            ('skirt', 'Skirt'),
        )
        ),
        ('Outwear', (
            ('cardigan', 'Cardigan'),
            ('coat', 'Coat'),
            ('jacket', 'Jacket'),
            ('vest', 'Vest'),
        )
        ),
        ('Shoes', (
            ('boots', 'Boots'),
            ('flats', 'Flats'),
            ('heels', 'Heels'),
            ('sandals', 'Sandals'),
            ('slippers', 'Slippers'),
            ('sneakers', 'Sneakers'),
        )
        ),
    ]

    class Colors(models.TextChoices):
        GREEN = 'green', _('Green')
        TURQUOISE = 'turqoise', _('Turqoise')
        BLUE = 'blue', _('Blue')
        PURPLE = 'purple', _('Purple')
        RED = 'red', _('Red')
        PINK = 'pink', _('Pink')
        ORANGE = 'orange', _('Orange')
        YELLOW = 'yellow', _('Yellow')
        WHITE = 'white', _('White')
        GREY = 'grey', _('Grey')
        BLACK = 'black', _('Black')
        BROWN = 'brown', _('Brown')
        MULTI = 'multi', _('Multi')

    class Source(models.TextChoices):
        BRAND_STORE = 'brand_store', _('Brand Store')
        DEPARTMENT_STORE = 'department_store', _('Department Store')
        DISCOUNT_STORE = 'discount_store', _('Discount Store')
        THRIFT_SHOP = 'thrift_shop', _('Thrift Shop')
        RESALE_CONSIGNMENT_SHOP = 'resale/consignment_shop', _(
            'Resale/Consignment Shop')
        FRIEND = 'friend', _('Friend')
        OTHER = 'other', _('Other')
    
    closet_item_id = models.CharField(max_length=50, default="None", primary_key=True)

    item_choice = models.CharField(
        max_length=50,
        choices=ITEM_CHOICES,
        blank=True,
        null=True)
    size = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        default="unknown")
    color = models.CharField(
        max_length=25,
        choices=Colors.choices,
        blank=True,
        null=True)
    material = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default="unknown")
    source = models.CharField(
        choices=Source.choices,
        max_length=50,
        blank=True,
        null=True,
        default="unknown")
    brand = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default="unknown")
    tag = TaggableManager(through=GenericStringTaggedClosetItem)
    item_image = models.ImageField(
        upload_to='closet_items/',
        blank=True,
        null=True)
    added_at = models.DateField(
        auto_now=True)
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE,
                             related_name='closet_items')

    def __str__(self):
        return f'{self.item_choice} in {self.color} by {self.brand}'


class Outfit(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='outfits')
    outfit_id = models.CharField(max_length=50, default="None", primary_key=True)
    closet_item = models.ManyToManyField(
        ClosetItem,
        related_name='outfits')
    title = models.CharField(
        max_length=100,
        blank=True,
        null=True)
    tag = TaggableManager(through=GenericStringTaggedOutfit)
    outfit_date = models.DateField(
        blank=True,
        null=True)
    outfit_image = models.ImageField(
        upload_to='outfits/',
        blank=True,
        null=True)
    draft = models.BooleanField(
        default=True)
    favorite = models.BooleanField(
        default=False)

    def __str__(self):
        return f'{self.title} created by {self.user}'
