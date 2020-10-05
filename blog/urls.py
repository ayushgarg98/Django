from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.BlogView.as_view(), name = 'blog'),
    path('entry/<int:pk>/', views.EntryView.as_view(), name = 'entry'),
    path('create_blog/', views.get_blog, name = 'get_blog'),
    path('saved/', views.saved, name = 'saved'),
    path('register/', views.register, name='register'),
]