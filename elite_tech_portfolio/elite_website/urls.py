from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from elite_website import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us/', views.contactus, name='contact-us'),
        ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
