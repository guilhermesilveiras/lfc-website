from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from django.views import generic


# Create your views here.

# home do blog

def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html', {
            "form": UserCreationForm
        })
    
    else:

        if request.POST['password1'] == request.POST['password2']:

            try:
                
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()

                login(request, user)
                return redirect('tasks')
            
            except:

                return render(request, 'signup.html', {
                'form' : UserCreationForm,
                'error' : 'Usuário já existe.'
                })
            
        return render(request, 'signup.html', {
            'form' : UserCreationForm,
            'error' : 'As senhas não coincidem.'
             })
    
def signin(request):

    if request.method == "GET":
        return render(request, 'signin.html', {
        'form': AuthenticationForm
        })
    
    else:
        
        user = authenticate (

            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                    'form': AuthenticationForm,
                    'error': 'Usuário ou senha inválidos.'
                })

        else:
                login(request, user)
                return redirect('tasks')
        
@login_required
def tasks(request):
    return render(request, 'tasks.html')

@login_required
def signout(request):
    logout(request)

    return redirect('home')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class DetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
