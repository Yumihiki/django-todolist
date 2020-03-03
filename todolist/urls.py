from django.urls import path

from . import views
from .views import ListToDoList, DetailToDoList

app_name = 'todolist'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/delete', views.DeleteView.as_view(), name='delete'),
    path('<int:pk>/update', views.UpdateView.as_view(), name='update'),
    path('create', views.CreateView.as_view(), name='create'),
    path('api/<int:pk>/', DetailToDoList.as_view())
]