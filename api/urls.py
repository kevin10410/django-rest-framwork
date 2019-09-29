from django.urls import path

from .views import StatusListAPIView, StatusDetailAPIView, StatusCreateAPIView, StatusUpdateAPIView

urlpatterns = [
  path('', StatusListAPIView.as_view()),
  path('<int:pk>/', StatusDetailAPIView.as_view()),
  path('create/', StatusCreateAPIView.as_view()),
  path('<int:pk>/update/', StatusUpdateAPIView.as_view()),
  # path('<int:id>/delete/', StatusDeleteAPIView.as_view()),
]
