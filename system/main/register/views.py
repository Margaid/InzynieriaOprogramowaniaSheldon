from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm,ProfileForm

# Create your views here.
'''
def register(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.customuser.firma = form.cleaned_data.get('firma')
            user.customuser.operator = form.cleaned_data.get('operator')
            user.save()
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=user.username, password=raw_password)
            #login(request, user)
            
            #przekierowanie na strone oczekiwania
            return redirect('register')
    else:
        form = SignUpForm()
    return render(request, 'register/register.html', {'form': form})

'''

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        p_reg_form = ProfileForm(request.POST)
        if form.is_valid() and p_reg_form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            p_reg_form = ProfileForm(request.POST, instance=user.profile)
            p_reg_form.full_clean()
            #user.customuser.firma = p_reg_form.cleaned_data.get('firma')
            #user.customuser.operator = p_reg_form.cleaned_data.get('operator')
            p_reg_form.save()
            #messages.success(request, f'Your account has been sent for approval!')
            return redirect('register.html')
    else:
        form = SignUpForm()
        p_reg_form = ProfileForm()
    
    return render(request, 'register/register.html', {
        'form': form,
        'p_reg_form': p_reg_form
    })



#def update_profile(request, user_id):
#    user = User.objects.get(pk=user_id)
#    user.save()