from django.contrib.auth.models import AbstractUser
from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _

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


class ClosetItem(models.Model):

    class Category(models.TextChoices):
        TOP = 'top', _('Top')
        BOTTOM = 'bottom', _('Bottom')
        OUTERWEAR = 'outerwear', _('Outerwear')
        SHOES = 'shoes', _('Shoes')

    class SubCategory(models.TextChoices):
        BUTTON_DOWN = 'button-down', _('Button-down')
        DRESS = 'dress', _('Dress')
        SHIRT = 'shirt', _('Shirt')
        SWEATER = 'sweater', _('Sweater')
        T_SHIRT = 't-shirt', _('T-shirt')
        PANTS = 'pants', _('Pants')
        SHORTS = 'shorts', _('Shorts')
        SKIRT = 'skirt', _('Skirt')
        CARDIGAN = 'cardigan', _('Cardigan')
        COAT = 'coat', _('Coat')
        JACKET = 'jacket', _('Jacket')
        VEST = 'vest', _('Vest')
        BOOTS = 'boots', _('Boots')
        FLATS = 'flats', _('Flats')
        HEELS = 'heels', _('Heels')
        SANDALS = 'sandals', _('Sandals')
        SLIPPERS = 'slippers', _('Slippers')
        SNEAKERS = 'sneakers', _('Sneakers')

    class Colors(models.TextChoices):
        WHITE = 'white', _('White')
        GREEN = 'green', _('Green')
        YELLOW = 'yellow', _('Yellow')
        ORANGE = 'orange', _('Orange')
        RED = 'red', _('Red')
        PINK = 'pink', _('Pink')
        PURPLE = 'purple', _('Purple')
        TURQUOISE = 'turqoise', _('Turqoise')
        BLUE = 'blue', _('Blue')
        BROWN = 'brown', _('Brown')
        BLACK = 'black', _('Black')
        GREY = 'grey', _('Grey')
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

    category = models.CharField(
        max_length=50,
        choices=Category.choices,
        null=True)
    subcategory = models.CharField(
        max_length=50,
        choices=SubCategory.choices,
        null=True)
    size = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        default="unknown")
    color = models.CharField(
        max_length=25,
        choices=Colors.choices,
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
    tag = TaggableManager(blank=True)
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
        return f'{self.subcategory} in {self.color} by {self.brand}'


class Outfit(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='outfits')
    closet_item = models.ManyToManyField(
        ClosetItem,
        related_name='outfits')
    title = models.CharField(
        max_length=100,
        blank=True,
        null=True)
    tag = TaggableManager(blank=True)
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
