from django.urls import path
from . import views

app_name = "accounts"
# path('nom_voulu/', views.view, name = 'nom'),
urlpatterns = [
    path('login_user/', views.login_user, name= 'login'),
    path('logout/', views.logout_user, name= 'logout'),
    path('register/',views.register_user, name= 'register'),
]