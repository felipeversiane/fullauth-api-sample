from django.urls import path, include, re_path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from myapp.urls import router as router_myapp
from account.urls import router as router_account
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Auth-Full API",
        default_version='v1',
        description="API made for a auth-full api backend challenge.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="felipeversiane09@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # DJOSER URLs
    path('api/', include('djoser.urls')),
    
    # Custom App URLs
    path('api/', include('account.urls')),
    path('api/', include('myapp.urls')),
    
    # DRF Routers for Apps
    path('api/', include(router_myapp.urls)),
    path('api/', include(router_account.urls)),

    # DRF Authentication URLs
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
