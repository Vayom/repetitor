from django.contrib import admin
from django.urls import path, include

from teaching.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth_sys/', include('auth_sys.urls')),
    path('teaching/', include('teaching.urls')),
    path('', home, name='home'),
]
