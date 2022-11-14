from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginPage,name='login'),
    path('register/',views.registerPage,name='register'),
    path('logout/',views.logoutPage,name='logout'),

    path('profile/<str:user_id>',views.profilePage,name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)