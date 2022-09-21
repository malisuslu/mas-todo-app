from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from todo.forms import TodoForm, UserForm
from todo.models import TodoItem, TodoUser
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
@method_decorator(login_required, name='dispatch') # Don't forget to add (LOGIN_URL = '/login') to settings.py
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

        datas = []
        todos = TodoItem.objects.filter(user=request.user)
        for todo in todos:
            datas.append({'todo': todo, 'form': TodoForm(instance=todo)})
        return render(request, 'todo/form.html', {'form': form, 'datas': datas})

    def post(self, request, id=None):
    
        if id==None:
            form = TodoForm(request.POST)
            form.instance.user = request.user # This line is important to add the user to the todo item when creating it
            
            #if priority is already taken for this user, then give an error message
            if TodoItem.objects.filter(user=request.user, priority=request.POST['priority']).exists():
                messages.error(request, 'Priority already taken!')
                return redirect('table')


            elif form.is_valid():
                form.save()
                messages.success(request, 'Todo item saved successfully')
                form = TodoForm()

        else:
            todo = TodoItem.objects.get(pk=id)
            form = TodoForm(request.POST, instance=todo)
            if form.is_valid():
                form.save()
                messages.success(request, 'Todo item updated successfully')
                form = TodoForm()

        return redirect('table')


# class Register(View):
#     def get(self, request):
#         form = UserCreationForm()
#         return render(request, 'registration/register.html', {'form': form})

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'User created successfully')
#             return redirect('login')
#         else:
#             messages.error(request, 'User not created')
#             return redirect('register')


# Alternative method with built-in CreateView



class Register(CreateView):
    form_class = UserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('table')

    def form_valid(self, form):
        valid = super(Register, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid