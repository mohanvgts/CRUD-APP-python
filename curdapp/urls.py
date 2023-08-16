from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.getUser),
     path('user/add/', views.createUser),
    path('user/<str:pk>/',views.getuserByID),
    path('user/update/<str:pk>/',views.updateUser),
    path('user/delete/<str:pk>/', views.deleteUser)
]
