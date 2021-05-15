from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm
from .models import Event
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from . import tasks


# AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/login_user/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'events'
    template_name = 'index.html'

    def get_queryset(self):
        print(self.request.user)
        return Event.objects.filter(user=self.request.user)


class EventCreate(LoginRequiredMixin, CreateView):
    login_url = '/login_user/'
    redirect_field_name = 'redirect_to'
    model = Event
    fields = ['title', 'event_type', 'detail', 'event_logo', 'date', 'time']
    template_name = 'create_event.html'

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(EventCreate, self).form_valid(form)


class EventDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/login_user/'
    redirect_field_name = 'redirect_to'
    model = Event
    template_name = 'detail.html'


class EventUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login_user/'
    redirect_field_name = 'redirect_to'
    model = Event
    fields = ['title', 'event_type', 'detail', 'event_logo', 'date', 'time']
    template_name = 'create_event.html'

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(EventUpdate, self).form_valid(form)


class EventDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login_user/'
    redirect_field_name = 'redirect_to'
    model = Event
    success_url = reverse_lazy('Event:index')


def favorite_event(request, event_id=None):
    event = get_object_or_404(Event, id=event_id)
    try:
        if event.is_favorite:
            event.is_favorite = False
        else:
            event.is_favorite = True
        event.save()
    except (KeyError, Event.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


class LogoutView(View):
    def get(self, request):
        logout(request)
        form = UserForm(request.POST or None)
        context = {
            "form": form,
        }
        return render(request, 'login.html', context)


class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                tasks.send_email('patel1451@gmail.com', 'welcome'+username)
                return redirect('Event:index')
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})

    def get(self, request):
        return render(request, 'login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('Event:index')
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)
