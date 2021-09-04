from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, FormView

from .forms import MyUserForm, MyUserEditForm, NumberstoWordsForm
import base64
from num2words import num2words

from .mixins import UserLoginRequiredMixin

User = get_user_model()


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class MyLoginView(LoginView):
    pass

PER_PAGE = ("10", "25", "50", "100", "200", "500",)


class EmployeesListView(LoginRequiredMixin, ListView):
    model = User
    paginate_by = 10
    ordering = ['-id']

    def get_queryset(self):
        query_set = super(EmployeesListView, self).get_queryset()
        return query_set.filter(is_employee=True)

    def get_context_data(self, *args, **kwargs):
        context = super(EmployeesListView, self).get_context_data(*args, **kwargs)
        context['per_page_list'] = PER_PAGE
        return context

    def get_paginate_by(self, queryset):
        """
        Paginate by specified value in querystring, or use default class property value.
        """
        per_page = int(self.request.GET.get('paginate_by', self.paginate_by))
        if queryset.count() < int(per_page):
            per_page = 0
        return per_page


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = MyUserForm
    success_url = reverse_lazy('employees:list')

    def form_valid(self, form):
        if form.is_valid():
            response = super(EmployeeCreateView, self).form_valid(form)
            password = self.request.POST.get('password', None)
            if password:
                self.object.set_password(password)
            if 'profile_pic' in self.request.FILES:
                image = self.request.FILES['profile_pic']
                encoded_string = base64.b64encode(image.read())
                self.object.image = encoded_string
            self.object.save()
            return response
        else:
            return self.render_to_response(self.get_context_data(form=form))


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('employees:list')


class EmployeeEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = MyUserEditForm
    success_url = reverse_lazy('employees:list')

    def form_valid(self, form):
        if form.is_valid():
            response = super(EmployeeEditView, self).form_valid(form)
            password = self.request.POST.get('password', None)
            email = self.request.POST.get('email', None)
            if password:
                self.object.set_password(password)
            if email:
                self.object.username = email
            if 'profile_pic' in self.request.FILES:
                image = self.request.FILES['profile_pic']
                encoded_string = base64.b64encode(image.read())
                self.object.image = encoded_string
            self.object.save()
            return response
        else:
            return self.render_to_response(self.get_context_data(form=form))


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = User


class NumbersInWords(FormView):
    form_class = NumberstoWordsForm
    template_name = 'numbers2words.html'
    success_url = reverse_lazy('numbers_to_words')

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        number = self.request.POST.get('enter_number')
        num_string = num2words(int(number), lang='en_IN')
        context['form'] = form
        context['in_words'] = num_string
        return self.render_to_response(context)
