from django.urls import path

from .views import StatusListAPIView, StatusDetailAPIView, StatusCreateAPIView, StatusUpdateAPIView, StatusDeleteAPIView

urlpatterns = [
  path('', StatusListAPIView.as_view()),
  path('<int:pk>/', StatusDetailAPIView.as_view()),
  path('create/', StatusCreateAPIView.as_view()),
  path('<int:pk>/update/', StatusUpdateAPIView.as_view()),
  path('<int:pk>/delete/', StatusDeleteAPIView.as_view()),
]
