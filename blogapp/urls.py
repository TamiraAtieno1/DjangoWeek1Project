from django.urls import path, include
from .views import home,create,detailed,update,delete
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blogapp'

urlpatterns = [
    path('', home, name="home"),
    path('create/', create, name="create"),
    path('detailed/<int:blog_id>', detailed, name="detailed" ),
    path('update/<int:blog_id>', update, name="update"),
    path('delete/<int:blog_id>', delete, name="delete"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)