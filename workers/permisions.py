from rest_framework import permissions
from .models import Worker

class IsWorkerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        print("User",request.user)
        print("Is Worker:",request.user.is_authenticated and request.user.is_worker)
        return request.user.is_authenticated and request.user.is_worker

        # user = request.user
        # is_authenticated_worker = user.is_authenticated and Worker.objects.filter(user=user.id, is_worker=True).exists()
        # is_worker = getattr(user, 'is_worker', False)
        # return is_authenticated_worker and is_worker



    # def has_permission(self, request, view):
#     print("User:", request.user)
#     print("Is Worker:", request.user.is_authenticated and request.user.is_worker)
#     return request.user.is_authenticated and request.user.is_worker