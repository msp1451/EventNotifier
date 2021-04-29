from django.urls import path
from . import views


app_name = 'Event'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.register, name='register'),
    path('login_user/', views.LoginView.as_view(), name='login_user'),
    path('logout_user/', views.LogoutView.as_view(), name='logout_user'),
    path('<int:pk>/', views.EventDetail.as_view(), name='detail'),
    path('create_event/', views.EventCreate.as_view(), name='create_event'),
    path('event/<int:pk>/', views.EventUpdate.as_view(), name='update_event'),
    path('<int:pk>/delete_event/', views.EventDelete.as_view(), name='delete_event'),
    path('<int:pk>/favorite_event/', views.favorite_event, name='favorite_event'),
]
