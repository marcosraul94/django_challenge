from django.urls import path
from .views import MusicalWorkDetailView

urlpatterns = [
    path('musical-work/<str:iswc>', MusicalWorkDetailView.as_view()),
]

