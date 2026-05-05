from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import (
    RestaurantViewSet,
    EmployeeCreateView,
    MenuCreateView,
    TodayMenuAPIView,
    VoteCreateView,
    ResultsAPIView
)

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)

urlpatterns = [
    path('register/', EmployeeCreateView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('menu/upload/', MenuCreateView.as_view(), name='menu-upload'),
    path('menu/today/', TodayMenuAPIView.as_view(), name='menu-today'),
    path('vote/', VoteCreateView.as_view(), name='vote'),
    path('results/', ResultsAPIView.as_view(), name='results'),
    path('', include(router.urls))
]
