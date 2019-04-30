from django.urls import path
from trip.routes import views as route_views

urlpatterns = [
    path('routes/', route_views.RouteAPIView.as_view()),
]
