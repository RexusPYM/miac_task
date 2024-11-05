from django.urls import path

from . import views

from .swagger import schema_view

app_name = "exchange"


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api_materials/<int:pk>', views.MaterialAPIView.as_view()),
    path('api_materials/', views.MaterialAPIView.as_view()),
    path('api_sellers/<int:pk>', views.SellerAPIView.as_view()),
    path('api_sellers/', views.SellerAPIView.as_view()),
]
