from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import LoginForm, SignupForm, EditProfileForm


class UserLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'accounts/login.html'

class SignupView(View):
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        context = {'SignupForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('profile')
        
        context = {'SignupForm': form}
        return render(request, self.template_name, context)

@method_decorator(decorator=login_required, name='get')
class UserProfileView(View):
    form_class = EditProfileForm
    template_name = 'accounts/profile.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)

        context = {'EditProfileForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Profile updated & successfully saved')
            return redirect('profile')
        
        context = {'EditProfileForm': form}
        return render(request, self.template_name, context)


class LogoutUser(LogoutView):
    template_name = 'accounts/logout.html'
