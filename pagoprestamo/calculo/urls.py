from django.urls import path
from .views import calculoView

urlpatterns = [
    path('calculoInteres', calculoView.as_view()),
]