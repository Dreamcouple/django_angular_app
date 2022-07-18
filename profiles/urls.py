from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProfileListAPIView.as_view(), name="profile"),
    path('<int:id>', views.ProfileDetailAPIView.as_view(), name="profile_detail"),
]