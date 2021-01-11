from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import UserRegistrationForm



class RegisterView(FormView):
    """ Create User """
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'account/registration.html'


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


    def form_invalid(self, form):
        return super().form_invalid(form)
