from django.views.generic import ListView
from django.shortcuts import render
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SingUpForm, UtworzWydarzenieForm, EventSearchForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UtworzWydarzenieForm

from .models import CreateWydarzenieModel


def hello(request):
    return HttpResponse('Hello, world!')


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SingUpForm
    success_url = reverse_lazy('hello')


class ListViewW(ListView):
    template_name = 'list.html'
    model = CreateWydarzenieModel
    context_object_name = 'events'
    ordering = ['deta_open']


@login_required
def create_event(request):
    if request.method == 'POST':
        form = UtworzWydarzenieForm(request.POST)
        if form.is_valid():
            # Przypisz aktualnie zalogowanego użytkownika jako właściciela wydarzenia
            form.instance.user_append = request.user
            form.save()
            return redirect('event_list')
    else:
        form = UtworzWydarzenieForm()
    return render(request, 'form.html', {'form': form})


def search_events(request):
    form = EventSearchForm(request.GET)
    events = CreateWydarzenieModel.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        search_type = form.cleaned_data.get('search_type')

        if query:
            events = events.filter(title__icontains=query)

        now = datetime.now().date()

        if search_type == 'future':
            events = events.filter(deta_open__gt=now)
        elif search_type == 'ongoing_future':
            events = events.filter(Q(deta_open__lte=now, deta_close__gte=now) | Q(deta_open__gt=now))

    return render(request, 'search_results.html', {'form': form, 'events': events})


print("napisanie z gita")

print("hello")
