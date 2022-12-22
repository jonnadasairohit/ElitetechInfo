from django.urls import path
from elite_website import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us/', views.contactus, name='contact-us'),
               ]