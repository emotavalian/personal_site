from django.urls import path
from . import views

# from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about_us', views.about_page_view, name='about'),
    path('contact_us', views.contact_page_view, name='contact'),
    path('login/', views.CustomLoginView.as_view(), name='account_login'),
]
