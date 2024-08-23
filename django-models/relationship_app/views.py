["relationship_app/list_books.html"]

["relationship_app/library_detail.html"]

["from django.views.generic.detail import DetailView"]
from django.shortcuts import render

# Create your views here.
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

#
from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

#

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

["from django.contrib.auth import login"]
class UserLoginView(LoginView):
    template_name = 'login.html'

["from django.contrib.auth import logout"]
class UserLogoutView(LogoutView):
    template_name = 'logout.html'

["from django.contrib.auth import register"]
class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
