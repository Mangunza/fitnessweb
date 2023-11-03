
from django.urls import path
from authapp import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('signup', views.signup, name="signup"),
    path('login', views.validarlogin, name="validarlogin"),
    path('logout', views.validarlogout, name="validarlogout"),
]
