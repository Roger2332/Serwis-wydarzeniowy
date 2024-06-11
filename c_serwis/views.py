from django.views.generic import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SingUpForm, UtworzWydarzenieForm

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
