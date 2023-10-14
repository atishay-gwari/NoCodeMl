from django.urls import path
import home.views as views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name='home'),
    

    path('login/', views.loginpage,name="login"),
    
    path('logout/',views.logoutpage,name='logout'),

    path('signup/', views.signuppage,name="signup"),


]
