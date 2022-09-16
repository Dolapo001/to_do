from django.views.generic import ListView
from .models import Task


class TodoListView(ListView):
    model = Task
    template_name = "home.html"
