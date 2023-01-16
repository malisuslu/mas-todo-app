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
                if todo.user_id == request.user.id:
                    todo.delete()
                    messages.success(request, 'Todo item deleted successfully')
                    return redirect('table')
                else:
                    messages.error(request, 'You are not authorized to delete this item')
                    return redirect('table')

            elif request.path == '/update/'+str(id):
                todo = TodoItem.objects.get(pk=id)
                if todo.user_id == request.user.id:
                    form = TodoForm(instance=todo)
                else:
                    messages.error(request, 'You are not allowed to update this todo item')
                    return redirect('table')

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

            #if priority is already taken for another todo item, then give an error message
            if TodoItem.objects.filter(user=request.user, priority=request.POST['priority']).exclude(pk=id).exists():
                messages.error(request, 'Priority already taken! Please choose another one.')
                return redirect('table')

            if form.is_valid():
                form.save()
                messages.success(request, 'Todo item updated successfully')
                form = TodoForm()

        return redirect('table')


# class Register(View):
#     def get(self, request):
#         form = UserForm()
#         return render(request, 'registration/register.html', {'form': form})

#     def post(self, request):
#         form = UserForm(request.POST)
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

# class UpdateUser(UpdateView):
#     form_class = UserForm
#     template_name = 'registration/update.html'
#     success_url = reverse_lazy('table')

#     def get_object(self):
#         return TodoUser.objects.get(pk=self.kwargs['id'])

# class DeleteUser(DeleteView):
#     model = TodoUser
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('table')



# class Update(UpdateView):
#     model = TodoItem
#     form_class = TodoForm
#     template_name = 'todo/update.html'
#     success_url = reverse_lazy('table')

#     def get(self, request, *args, **kwargs):
#         todo = TodoItem.objects.get(pk=kwargs['pk'])
#         if todo.user_id == request.user.id:
#             return super(Update, self).get(request, *args, **kwargs)
#         else:
#             messages.error(request, 'You are not allowed to update this todo item')
#             return redirect('table')

# class Delete(DeleteView):
#     model = TodoItem
#     template_name = 'todo/delete.html'
#     success_url = reverse_lazy('table')

#     def get(self, request, *args, **kwargs):
#         todo = TodoItem.objects.get(pk=kwargs['pk'])
#         if todo.user_id == request.user.id:
#             return super(Delete, self).get(request, *args, **kwargs)
#         else:
#             messages.error(request, 'You are not allowed to delete this todo item')
#             return redirect('table')