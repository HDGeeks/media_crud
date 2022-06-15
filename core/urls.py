
from django.contrib import admin
from django.urls import path ,include
from rest_framework import permissions
from django.conf.urls.static import static
from . import settings

# api documentation
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

schema_view = get_schema_view(
    # API schema for our accounts

    openapi.Info(
      title="Media-CRUD API",
      default_version='v1',
      description="user accounts API description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="dannyhd88@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),

)

urlpatterns = [
    path('admin/', admin.site.urls),
     # API documentation urls
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('', include('app_kin_media.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
