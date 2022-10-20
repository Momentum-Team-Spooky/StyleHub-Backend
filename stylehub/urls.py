from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from stylehub import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.api_root),
    path('mycloset/', views.MyClosetList.as_view(), name='my-closet-items'),
    path('mycloset-tops/', views.MyClosetListTops.as_view(), name='my-closet-tops'),
    path('mycloset-bottoms/', views.MyClosetListBottoms.as_view(),
         name='my-closet-bottoms'),
    path('mycloset-outerwear/', views.MyClosetListOuterwear.as_view(),
         name='my-closet-outerwear'),
    path('mycloset-shoes/', views.MyClosetListShoes.as_view(),
         name='my-closet-shoes'),
    path('closet-item/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('myoutfits/', views.MyOutfitList.as_view(), name='my-outfits'),
    path('outfit/<int:pk>/', views.OutfitDetail.as_view(), name='outfit'),
    path('outfit-detail/<int:pk>/',
         views.OutfitDetailEdit.as_view(), name='outfit-detail'),
    path('myprofile/', views.UserProfile.as_view(), name='my-profile'),
    path('profile/<int:pk>/', views.UserDetail.as_view(), name='profile-detail'),
    path('outfits/favorite/', views.FavoriteOutfitsList.as_view(),
         name='favorite-outfits'),
    path('closet-composition/', views.ClosetComposition.as_view(),
         name='closet-composition'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
