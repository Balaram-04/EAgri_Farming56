from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/',views.Contact,name="Contact"),
    path('query/',views.query_form, name='query_form'),
    path('blogs/',views.blog_list, name='blog_list'),
    path('blogs/add/', views.add_blog, name='add_blog'),
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('delete-blog/<int:blog_id>/',views.delete_blog, name='delete_blog'),
]