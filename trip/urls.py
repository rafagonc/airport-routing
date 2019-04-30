from django.urls import path
from django.views.generic import TemplateView
from trip.routes import views as route_views

urlpatterns = [
    path('routes/', route_views.RouteAPIView.as_view()),
    path('docs/', TemplateView.as_view(template_name="docs.html")),

]
