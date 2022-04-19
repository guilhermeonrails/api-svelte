from django.contrib import admin
from django.urls import path, include
from ingrediente.views import IngredienteViewSet, ReceitaViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="API de Ingredientes e receitas",
      default_version='v1',
      description="Provedor local de ingredientes e receitas desenvolvida pela Alura para o curso de Svelte",
      terms_of_service="#",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('ingredientes', IngredienteViewSet, basename='Ingredientes')
router.register('receitas', ReceitaViewSet, basename='Receitas')

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
