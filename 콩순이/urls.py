from django.urls import path

from 콩순이 import views

app_name = '콩순이'


urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list'),
    path('detail/<int:pk>/', views.CharacterDetailView.as_view(), name='character_detail'),
    path('create/', views.CharacterCreateView.as_view(), name='character_create'),
]