from django.shortcuts import render, get_object_or_404
from .models import Todo
from django.utils import timezone
from django.template import Context
# Create your views here.

def index(request):
    context = {
        'Exist': 1,
        'objs': 0
    }

    try:
        objs = Todo.objects.all()
        context['objs'] = objs

    except (KeyError, Todo.DoesNotExist):
        context['Exist'] = False

    if request.POST:
        item = request.POST['item']
        todo = Todo(text = item, added_date = timezone.now())
        todo.save()
    return render(request, "main/index.html", context)
