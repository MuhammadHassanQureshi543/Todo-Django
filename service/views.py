from django.shortcuts import render,HttpResponse,redirect
from service.models import todo
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    if request.method == "POST":
        title = request.POST.get('task')
        todo.objects.create(title=title)
        print(title)

    data = todo.objects.all()
    content = {
        'data':data
    }
    return render(request,'index.html',content)

def update(request):
    if request.method == "POST":
        id = request.POST.get('task_id')
        new_title = request.POST.get('new_title')
        obj = get_object_or_404(todo, id=id)
        obj.title = new_title
        obj.save()
        print(id,new_title)
        return redirect('/')
    return redirect('/')

def delte(request):
    if request.method == "POST":
        id = request.POST.get('obj_id')
        new_title = request.POST.get('obj_title')
        obj = get_object_or_404(todo, id=id)
        obj.delete()
        return redirect('/')
    return redirect('/')
