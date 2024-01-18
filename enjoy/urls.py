from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from rest_framework.authtoken import views
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from drf_yasg.views import  get_schema_view
from drf_yasg import openapi
from workers.views import logout_view


schema_view = get_schema_view(
   openapi.Info(
      title="Media API",
      default_version='v1',
      description="Social.media",
      contact=openapi.Contact(email="ismatilloismatov1995@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/api-auth",include('rest_framework.urls')),
    path('api/',include('workers.urls')),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/register/', include('dj_rest_auth.registration.urls')),
    path('api/logout',logout_view,name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger<format>.json|.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')

    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
