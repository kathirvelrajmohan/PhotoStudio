from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('view/<str:pk>/',views.viewPhoto,name = "view-photo"),
    path('register/',views.register,name = "register"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('update/<str:pk>/',views.updateImg,name="update"),
    path('delete/<str:pk>/',views.delete,name="delete"),
    path('search/',views.search,name="search"),
    path('userdetails/',views.userdetails,name="userdetails"),
    path('editProfileImage/',views.editProfileImage,name="editProfileImage"),
    path('editProfile/',views.editProfile,name="editProfile"),
    path('myPhotos/',views.myPhotos,name="myPhotos")



]