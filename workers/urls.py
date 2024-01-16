from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import WorkerViewSets,ProductViewSets


app_name = 'workers'

router = DefaultRouter()

router.register('workers',WorkerViewSets,basename='workers'),
router.register('products',ProductViewSets,basename='products'),



urlpatterns = [
    path('',include(router.urls))
]