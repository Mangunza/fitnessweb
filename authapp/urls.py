
from django.urls import path
from authapp import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('signup', views.signup, name="signup"),
    path('login', views.validarlogin, name="validarlogin"),
    path('logout', views.validarlogout, name="validarlogout"),
    path('contact', views.contact, name="contact"),
    path('join', views.enroll, name="enroll"),
    path('profile', views.profile, name="profile"),
    path('gallery', views.gallery, name="gallery"),
    path('attendance', views.attendance, name="attendance"),
]
