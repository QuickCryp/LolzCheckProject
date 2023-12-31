from django.urls import path
from .views import login_view, register_view, logout_view

app_name = 'auth'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('registration/', register_view, name='registration'),
    path('logout/', logout_view, name='logout'),
]