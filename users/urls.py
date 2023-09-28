from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    home_view,
    login_view,
    logout_view,
    registeration_view,
    search_view
)

app_name = 'users'

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', registeration_view, name='register'),
    path('search/', search_view, name='search')
]
 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
