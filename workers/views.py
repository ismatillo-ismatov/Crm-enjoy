from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny

from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token
from .models import Worker,Product,CustomUser
from .serializer import WorkerSerializer,ProductSerializer,CustomUserSerializer
from .permisions import IsWorkerPermission


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    request.auth.delete()
    return Response(data={'message': 'Logout successful'}, status=status.HTTP_200_OK)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]





class WorkerViewSets(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsWorkerPermission]



