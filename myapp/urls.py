from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
   
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('update', views.image_upload_view,name='main'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
]