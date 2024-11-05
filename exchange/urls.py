from django.urls import path
from . import views

app_name = "exchange"


urlpatterns = [
    path('api_materials/<int:pk>', views.MaterialAPIView.as_view()),
    path('api_materials/', views.MaterialAPIView.as_view()),
    path('api_sellers/<int:pk>', views.SellerAPIView.as_view()),
    path('api_sellers/', views.SellerAPIView.as_view()),
]
