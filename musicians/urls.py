from django.urls import path
from .views import MusicianList, MusicianDetail

urlpatterns = [
    path('', MusicianList.as_view(), name='musician_list'),
    path('<int:pk>/', MusicianDetail.as_view(), name='musician_detail'),
]


