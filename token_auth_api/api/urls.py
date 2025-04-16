from django.urls import path
from .views import SecureHelloView

urlpatterns = [
    path('secure-hello/', SecureHelloView.as_view()),
]