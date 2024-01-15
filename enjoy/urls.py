from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views
# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('djoser.urls')),
    path('api/v1/',include('djoser.urls.authtoken')),
    path('api/v1/',include('lead.urls')),
    path('api/v1/',include('team.urls')),
    path("api/v1/api-auth",include('rest_framework.urls')),
    # path('api/dj-rest-auth/register/', include('dj_rest_auth.registration.urls')),
]
