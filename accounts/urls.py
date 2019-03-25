from django.urls import path,include

#case 1. use this
#from . import views
# urlpatterns = [
# 	path('',views.home,name='account-home')
# ]

#case 2. use case 1 or use this
from .views import home,register
from django.contrib.auth.views import LoginView,LogoutView 

urlpatterns = [
	path('',home,name='account-home'),
	path('login/', LoginView.as_view(template_name='accounts/login.html')),
	path('logout/',LogoutView.as_view(template_name='accounts/logout.html')),
	path('register/',register,name='register'),
]
