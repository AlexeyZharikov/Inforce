from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from datetime import date
from .models import Restaurant, Menu, Vote
from .serializers import (
    RestaurantSerializer,
    MenuSerializer,
    VoteSerializer,
    UserSerializer
)


class EmployeeCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuCreateView (generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class TodayMenuAPIView(generics.ListAPIView):
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Menu.objects.filter(date=date.today())


class VoteCreateView(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user)


class ResultsAPIView(generics.GenericAPIView):
    def get(self, request):
        version = request.version
        today = date.today()
        results = (
            Menu.objects
            .filter(date=today)
            .annotate(votes_count=Count('vote'))
        )
        data = [
            {
                "restaurant": m.restaurant.name,
                "votes": m.votes_count,
                "date": m.date
            } for m in results
        ]
        if version == '1.0':
            return Response({"version": version, "results": data})
        elif version == '2.0':
            return Response({"version": version, "results": data})
