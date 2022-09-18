from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from todo.forms import TodoForm
from todo.models import TodoItem

# Create your views here.
class app(View):
    def get(self, request, id=None):
        if id==None:
            form = TodoForm()
        else:
            if request.path == '/delete/'+str(id):
                todo = TodoItem.objects.get(pk=id)
                todo.delete()
                messages.success(request, 'Todo item deleted successfully!')
                return redirect('table')

            elif request.path == '/update/'+str(id):
                todo = TodoItem.objects.get(pk=id)
                form = TodoForm(instance=todo)

        data = []
        todos = TodoItem.objects.all()
        for todo in todos:
            data.append({'todo': todo, 'form': TodoForm(instance=todo)})

        return render(request, 'todo/table.html', {'form': form, 'data': data})


    def post(self, request, id=None):
    
        if id==None:
            form = TodoForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Todo item saved successfully')
                form = TodoForm()
            else:
                messages.error(request, 'Todo item not saved')

        else:
            todo = TodoItem.objects.get(pk=id)
            form = TodoForm(request.POST, instance=todo)
            if form.is_valid():
                form.save()
                messages.success(request, 'Todo item updated successfully')
                form = TodoForm()
            else:
                messages.error(request, 'Todo item not updated')

        return redirect('table')