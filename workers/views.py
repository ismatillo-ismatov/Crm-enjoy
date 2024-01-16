from rest_framework.response import Response
from rest_framework import viewsets,permissions
from .models import Workers,Product
from .serializer import WorkerSerializer,ProductSerializer

class WorkerViewSets(viewsets.ModelViewSet):
    queryset = Workers.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()


class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()