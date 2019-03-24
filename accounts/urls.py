from django.urls import path,include

#case 1. use this
#from . import views
# urlpatterns = [
# 	path('',views.home,name='account-home')
# ]

#case 2. use case 1 or use this
from .views import home
urlpatterns = [
	path('',home,name='account-home')
]
