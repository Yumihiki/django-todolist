from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import ToDoList


class IndexView(ListView):

    model = ToDoList
    queryset = ToDoList.objects.order_by('-created_date')
    paginate_by = 20


class DetailView(DetailView):
    model = ToDoList


class DeleteView(DeleteView):
    model = ToDoList

    success_url = reverse_lazy('todolist:index')


class CreateView(CreateView):
    model = ToDoList

    fields = ['author', 'title', 'content', 'created_date'] 
    success_url = reverse_lazy('todolist:index')


class UpdateView(UpdateView):
    model = ToDoList

    # updated_dateで更新日を入れる方法は？
    fields = ['author', 'title', 'content', 'status', 'updated_date'] 
    success_url = reverse_lazy('todolist:index')
