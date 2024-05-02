from django.urls import path
from .views import yangiliklar_view, get_yangilik, contact_view, about_view, texno_news_view

urlpatterns = [
    path('', yangiliklar_view, name='home_page'),
    path('texnologiya/', texno_news_view, name='texno_page'),
    path('<int:id>', get_yangilik, name='news_page'),
    path('contact-us/', contact_view, name='contact_page'),
    path('about/', about_view, name='about_page')
]
