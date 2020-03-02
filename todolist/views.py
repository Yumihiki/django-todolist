from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import ToDoList


class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'message' : "Hello,world",
        }
        return render(request, 'index.html', context)


index = IndexView.as_view()


class ToDoListView(ListView):

    model = ToDoList
    queryset = ToDoList.objects.order_by('-created_date')
    paginate_by = 20


class ToDoListDetailView(DetailView):

    model = ToDoList

