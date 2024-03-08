from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from teaching.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth_sys/', include('auth_sys.urls')),
    path('teaching/', include('teaching.urls')),
    path('api_teaching/', include('api_teaching.urls')),
    path('', home, name='home'),
]

if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
