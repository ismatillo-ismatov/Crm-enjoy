from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet,get_team,add_member

router = DefaultRouter()
router.register('teams',TeamViewSet,basename='teams')

urlpatterns = [
    path('teams/get_team/', get_team, name='get_team'),
    path('teams/add_member/', add_member, name='add_member'),
    path('',include(router.urls)),
]