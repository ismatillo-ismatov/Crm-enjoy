from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import WorkerViewSets,ProductViewSet,CustomUserViewSet



router = DefaultRouter()

router.register(r'users',CustomUserViewSet)
router.register(r'workers',WorkerViewSets,basename='worker'),
router.register(r'products',ProductViewSet),



urlpatterns = [
    path('',include(router.urls)),
    # path('add-products',ProductListCreateView.as_view(),name='add-products'),
    # path('products/', ProductListCreateView.as_view(), name='products')
]