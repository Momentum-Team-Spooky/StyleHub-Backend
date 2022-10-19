from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from stylehub import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.api_root),
    path('mycloset/', views.MyClosetList.as_view(), name='my-closet-items'),
    path('closet-item/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('myoutfits/', views.MyOutfitList.as_view(), name='my-outfits'),
    path('outfit/<int:pk>/', views.OutfitDetail.as_view(), name='outfit-detail'),
    path('myprofile/', views.UserProfile.as_view(), name='my-profile'),
    path('profile/<int:pk>/', views.UserDetail.as_view(), name='profile-detail'),
    path('outfits/favorite/', views.FavoriteOutfitsList.as_view(),
         name='favorite-outfits'),
    path('closet-composition/', views.ClosetComposition.as_view(),
         name='closet-composition'),
    # path('source-composition/', views.SourceComposition.as_view(),
    #      name='source-composition'),
    # path('brand-composition/', views.BrandComposition.as_view(),
    #      name='brand-composition'),
    # path('tag-composition/', views.TagComposition.as_view(),
    #      name='tag-composition'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
