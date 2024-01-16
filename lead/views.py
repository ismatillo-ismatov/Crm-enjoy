from rest_framework import viewsets
from django.contrib.auth.models import User
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

    def perform_update(self, serializer):
        obj = self.get_object()
        member_id = self.request.data['assigned_to']
        if member_id:
            user = User.objects.get(pk=member_id)
            serializer.save(assigned_to=user)
        else:
            serializer.save()