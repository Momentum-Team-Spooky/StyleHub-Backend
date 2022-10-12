from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from stylehub import views

urlpatterns = [
    path('', views.api_root),
    path('mycloset/', views.MyClosetList.as_view(), name='my-closet-items'),
    path('closet-item/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('myoutfits/', views.MyOutfitList.as_view(), name='my-outfits'),
    path('outfit/<int:pk>/', views.OutfitDetail.as_view(), name='outfit-detail'),
]
