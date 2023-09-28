from django.urls import path
from . import views

urlpatterns = [
    path('<slug:query>', views.SearchPage.as_view(), name='search-query')
]