from django.shortcuts import render, redirect
from .decorators import user_required, operator_required, admin_required,superadmin_required
from django.contrib.auth.models import User
from register.models import Profile
from .forms import ProfileForm_for_admin
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseBadRequest, JsonResponse
from django.core.serializers import serialize
import json
from itertools import chain
from django.core import serializers
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form


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

@operator_required
def operator(response):
    return render(response, 'users_pages/operator.html')

@admin_required
def admin(response):
    return render(response, 'users_pages/admin.html')    

@superadmin_required
def superuser(request):
    users = User.objects.all()
    #id=request.GET.get("id_for_django_view")
    #user=User.objects.get(id=2)
    
    '''
    if request.is_ajax():
        id = request.GET.get('id', '')
        user = User.objects.get(id=id)
        data={
        'is_user': user.profile.is_user,
        'is_operator': user.profile.is_operator,
        'is_admin': user.profile.is_admin,
        'firm': user.profile.firm,
         }
        form = ProfileForm_for_admin(initial=data,instance=user)

        # send back whatever properties you have updated
        json_response = {'form': form}

        return HttpResponse(json.dumps(json_response),
            content_type='application/json')
'''
   # if request.method == 'POST':
        
    #    form = ProfileForm_for_admin(request.POST,instance=request.user)
     #   if form.is_valid():
     #       form.save()
            #user.refresh_from_db()  
           # p_reg_form = ProfileForm(request.POST, instance=user.profile)
           # p_reg_form.full_clean()
          #  p_reg_form.save()
            #messages.success(request, f'Your account has been sent for approval!')
           # return redirect('waiting/')
  #  else:
   #     form = ProfileForm_for_admin(instance=request.user)

    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    id=0
    if is_ajax:
        if request.method == 'GET':
            id = request.GET.get("id", None)
            if User.objects.filter(id = id).exists():
                user = User.objects.filter(id = id).values()
                profile=Profile.objects.filter(id = id).values()
                #pola do zmiany przy zatwierdzeniu 
                user2 = User.objects.get(id=id)
                data={
                'is_user': user2.profile.is_user,
                'is_operator':user2.profile.is_operator,
                'is_admin': user2.profile.is_admin,
                
                # tu zmienić na operatorów
                'firm': user2.profile.firm,
                }
                form = ProfileForm_for_admin(initial=data,instance=user2,prefix="Userdata")
                userr=user2.__dict__

                ctx = {}
                ctx.update(csrf(request))

                form_html = render_crispy_form(form, context=ctx)

              #  if form.is_valid():
                #    form.cleaned_data
                 # json_response={'context': list(chain(user,profile)),'form':form}
                #return JsonResponse({'context': list(chain(user,profile)),'form':list(userr)},safe=False)
                return JsonResponse({'context': list(chain(user,profile)),'form':form_html},safe=False)
                #data = serializers.serialize('json', self.get_queryset())
               # userr = User.objects.get(id=id)
               # return HttpResponse(json.dumps({'context': user}))
                #return JsonResponse(json.dumps(json_response))
        return JsonResponse({'status': 'Invalid request'}, status=400)

    if is_ajax:
        
        if request.method == 'PUT':

            data = json.load(request)
            id = data.get('id')


            todo = get_object_or_404(User, id=id)
           # data = json.load(request)
          #  updated_values = data.get('payload')

          #  todo.task = updated_values['task']
          #  todo.completed = updated_values['completed']
         #   todo.save()

            return JsonResponse({'status': 'git'})
        return JsonResponse({'status': 'Invalid request'}, status=400)


    return render(request, 'users_pages/superadmin.html',{'users':users,})  

