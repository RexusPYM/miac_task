from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="ExchangeAPI",
      default_version='v0.0.0.0.1',
      description="Здесь представлен API для управления материалами и продавцами биржы ",
      contact=openapi.Contact(email="praushkov.d@gmail.com"),
      license=openapi.License(name="Лицензия супер биржи"),
   ),
   public=True
)
