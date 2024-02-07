from django.contrib.auth.views import LoginView
from django.urls import path

from auth_sys.views import logout_view, RegisterView, about_me

app_name = 'auth_sys'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='auth_sys/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('about_me/', about_me, name='about_me'),
    path('register/', RegisterView.as_view(), name='register'),

]