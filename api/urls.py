from django.urls import path
from .views import ClassifyNumberView

urlpatterns = [
    path('classify/', ClassifyNumberView.as_view())
]
