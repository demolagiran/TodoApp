from django.shortcuts import render, redirect
from .models import Mytodo
from .forms import Todoform

def alltodos(request):
    tasks = Mytodo.objects.all()
    form = Todoform()
    if request.method == 'POST':
        form = Todoform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'alltodo.html',{'tasks' : tasks, 'form' : form})


def deleteItem(request, pk):
    task = Mytodo.objects.get(id = pk)
    task.delete()
    return redirect('alltodos')

def updateItem(request, pk):
    todo = Mytodo.objects.get(id = pk)
    updateForm = Todoform(instance= todo)
    if request.method == 'POST':
        updateForm = Todoform(request.POST, instance=todo)
        if updateForm.is_valid():
            updateForm.save()
        return redirect('alltodos')
    return render(request, 'updateItem.html', {'todo' : todo, 'updateform' : updateForm})

