from django.urls import path

from . import views

app_name = 'todolist'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('todolist/', views.ToDoListView.as_view(), name='todolist'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
]