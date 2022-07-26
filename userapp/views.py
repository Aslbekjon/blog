from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import RegisterForm, ProfileUpdateForm
from.models import UserProfile
from blogapp.views import BasicView

class Users(BasicView, View):
    def get(self,request):


        context={
            'users':UserProfile.objects.all(),
            'categories': self.category(),
            'tags': self.tag(),
        }
        return render(request,'userapp/users.html',context)

class LoginView(BasicView,View):
    def get(self,request):
        context = {
            'categories':self.category(),
            'tags':self.tag(),
        }
        return render(request,'userapp/login.html', context)
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'userapp/login.html')

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')

class RegisterView(BasicView,CreateView):
    form_class = RegisterForm
    template_name = 'userapp/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return context

class ProfileView(BasicView, View):
    def get(self,request):
        username = request.user.username
        user = UserProfile.objects.get(username=username)

        context = {
            'categories':self.category(),
            'tags':self.tag(),
            'user':user,
        }
        return render(request, 'userapp/profile.html', context)

class UserDetail(BasicView, View):
    def get(self, request, pk):
        user = UserProfile.objects.get(pk=pk)

        context = {
            'categories': self.category(),
            'tags': self.tag(),
            'user1': user,
        }
        return render(request, 'userapp/user_detail.html', context)

class ProfileUpdate(BasicView, UpdateView):
    form_class = ProfileUpdateForm
    template_name = "userapp/profile_update.html"
    success_url = reverse_lazy('profile')


    def get_object(self):
        return UserProfile.objects.get(username=self.request.user.username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return context

class ProfileDelete(BasicView, DeleteView):
    model = UserProfile
    template_name = "userapp/user_delete.html"
    success_url = reverse_lazy('users')

    def get_object(self):
        return UserProfile.objects.get(username=self.request.user.username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return context