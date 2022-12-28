from django.shortcuts import render, redirect
from .decorators import user_required
# Create your views here.



def page(request):
    user=request.user
    if user.profile.is_user and user.is_authenticated:
        return redirect('user/')
    elif user.profile.is_operator and user.is_authenticated:
        return redirect('operator/')    
    elif user.profile.is_admin and user.is_authenticated:
        return redirect('admin/')    
    elif user.is_superuser and user.is_authenticated:
        return redirect('superuser/')
    else:
        #tu dać stronę 404 albo żeby się zalogować
        return render(request, 'base/base.html' ) 

       
@user_required
def user(response):
    return render(response, 'users_pages/user.html')

def operator(response):
    return render(response, 'users_pages/operator.html')

def admin(response):
    return render(response, 'users_pages/admin.html')    

def superuser(response):
    return render(response, 'users_pages/superadmin.html')  