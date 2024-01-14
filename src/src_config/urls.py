from django.urls import re_path, path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from myapp.urls import router as router_myapp
from account.urls import router as router_account



urlpatterns = [
    re_path('admin/', admin.site.urls),
    
    path('api/', include('djoser.urls')),

    path('api/',include('account.urls')),
    path('api/',include('myapp.urls')),

    re_path(r'api/', include(router_myapp.urls)),
    re_path(r'api/', include(router_account.urls)),

    re_path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)