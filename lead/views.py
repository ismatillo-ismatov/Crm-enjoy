from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Lead
from team.models import Team
from .serializers import LeadSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        # filtered_queryset = self.queryset.filter(team=team,created_by=self.request.user)
        return self.queryset.filter(team=team)

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return serializer.save(team=team,created_by=self.request.user)
