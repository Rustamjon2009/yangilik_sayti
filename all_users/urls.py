from django.urls import path
from .views import get_users, users_view

urlpatterns = [
    path('foydalanuvchilar', users_view, name='users_page'),
    path('<str:name>', get_users, name='user_info_page'),
]
