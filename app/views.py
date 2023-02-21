from django.shortcuts import render
from extra_views import SearchableListMixin
from django.contrib.auth.models import User
from extra_views import *
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class CreateUserView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'createuser.html'
    
class MyView(View):
    def get(self, request):
        my_model = User.objects.all()
        context = {'my_model': my_model}
        return render(request, 'itemlist.html', context)
    

class UserListView(SearchableListMixin, ListView):
    model = User
    template_name = "Search.html"
    search_fields = ['username', 'email']