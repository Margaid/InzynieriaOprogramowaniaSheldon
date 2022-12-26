from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm,ProfileForm

# Create your views here.

def home(response):
    return render(response, 'home/home.html')

#rejestracja użytkownika
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        p_reg_form = ProfileForm(request.POST)
        if form.is_valid() and p_reg_form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            p_reg_form = ProfileForm(request.POST, instance=user.profile)
            p_reg_form.full_clean()
            p_reg_form.save()
            #messages.success(request, f'Your account has been sent for approval!')
            return redirect('waiting/')
    else:
        form = SignUpForm()
        p_reg_form = ProfileForm()
    
    return render(request, 'register/register.html', {
        'form': form,
        'p_reg_form': p_reg_form
    })



#def login(response):
 #   return render(response,'registration/login.html')

def waiting(response):
    return render(response, 'waiting/waiting.html')

def rodo(response):
    return render(response, 'register/rodo.html')
