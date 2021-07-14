from django.shortcuts import render, get_object_or_404
from .models import Todo
from django.utils import timezone
from django.template import Context
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    context = {
        'Exist': 1,
        'objs': 0,
        'year': timezone.now().year
    }

    try:
        objs = Todo.objects.all().order_by('-added_date')
        context['objs'] = objs

    except (KeyError, Todo.DoesNotExist):
        context['Exist'] = 0

    return render(request, "main/index.html", context)


def add_to(request):
    item = request.POST['item']
    if item not in '':
        todo = Todo(text = item, added_date = timezone.now())
        todo.save()
    return HttpResponseRedirect(reverse("main:index"))

@csrf_exempt
def delete_item(request, item_id):
    Todo.objects.get(id = item_id).delete()
    return HttpResponseRedirect(reverse("main:index"))
