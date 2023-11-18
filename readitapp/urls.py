from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexView.as_view(), name='home'),
    path('about/',AboutView.as_view(), name='about'),
    path('contact/',ContactView.as_view(), name='contact'),
    path('blog/',BlogView.as_view(), name='blog'),
    path('<int:pk>/',BlogSingleView.as_view(), name='blog_single'),
    path('login/',LoginView.as_view(), name='login'),
    path('register/',RegisterView.as_view(), name='register'),
    path('logout/',logout_user, name='logout'),
]