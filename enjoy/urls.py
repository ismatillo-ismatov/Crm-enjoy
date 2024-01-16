from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
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
    path('api/v1/',include('workers.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),

    path('api/v1/dj-rest-auth/register/', include('dj_rest_auth.registration.urls')),
    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
























# from dj_rest_auth.registration.views import RegisterView,ConfirmEmailView

# path('api/v1/dj-rest-auth/register/', RegisterView.as_view(), name='dj_rest_auth_register'),
# path('confirm-email/', ConfirmEmailView.as_view(), name='account_confirm_email'),