from django.urls import path
from app.views import *
from app.forms import *
urlpatterns = [
    path('', MyView.as_view(),name='home'),
    path('Search/', UserListView.as_view(),name='Search'),
    path('create/', CreateUserView.as_view(),name='createuser'),
]