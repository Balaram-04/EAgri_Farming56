from django.urls import path
from . import views
from django.conf import settings # new
from  django.conf.urls.static import static 

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/',views.Contact,name="Contact"),
    path('query/',views.query_form, name='query_form'),
    path('blogs/',views.blog_list, name='blog_list'),
    path('blogs/add/', views.add_blog, name='add_blog'),
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('delete-blog/<int:blog_id>/',views.delete_blog, name='delete_blog'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
