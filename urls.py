from django.urls import path
from .import views
import django_filters

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),


    

    path('', views.dashboard, name= "dashboard"),
    path('delete/<int:id>/', views.delete_data, name = "deletedata"),
    path('/<int:id>/', views.update_data, name = "updatedata"),
    path('at/', views.attendence, name="at"),
]
