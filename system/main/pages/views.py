from django.shortcuts import render, redirect
from .decorators import user_required, operator_required, admin_required,superadmin_required
from django.contrib.auth.models import User
from register.models import Profile
from .forms import ProfileForm_for_admin
from django.http import JsonResponse
import json
from itertools import chain
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form

#wybranie strony w zależności od rodzaju użytkownika
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

#strona użytkownika       
@user_required
def user(response):
    return render(response, 'users_pages/user.html')

#strona operatora
@operator_required
def operator(response):
    return render(response, 'users_pages/operator.html')

#strona admina
@admin_required
def admin(request):
    users = User.objects.all()

    #przekazanie niezatwierdzonych użytkowników
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            id = request.GET.get("id", None)
            if User.objects.filter(id = id).exists():
                user = User.objects.filter(id = id).values()
                profile=Profile.objects.filter(id = id).values()

                #pola do zmiany przy zatwierdzeniu/odrzuceniu
                user2 = User.objects.get(id=id)
                data={
                'is_user': user2.profile.is_user,
                'is_operator':user2.profile.is_operator,
                'is_admin': user2.profile.is_admin,
                'operator': user2.profile.operator,
                }
                form = ProfileForm_for_admin(initial=data,instance=user2)
                ctx = {}
                ctx.update(csrf(request))

                form_html = render_crispy_form(form, context=ctx)

                return JsonResponse({'context': list(chain(user,profile)),'form':form_html},safe=False)
        return JsonResponse({'status': 'Invalid request'}, status=400)
    

    #zatwierdzenie użytkownika
    is_ajax2 = request.headers.get('X-Requested-With') == 'XMLHttpRequest2'
    if is_ajax2:
        if request.method == 'PUT':
            data = json.load(request)
            updated_values = data.get('formData')
            id=updated_values['id']

            user = User.objects.get(id=id)
            user.profile.is_user=updated_values['is_user']
            user.profile.is_operator=updated_values['is_operator']
            user.profile.is_admin=updated_values['is_admin']
            user.profile.operator=updated_values['operator']
            user.profile.approval=1
            user.save()

            return JsonResponse({'id':id,})
        return JsonResponse({'status': 'Invalid request'}, status=400)


    #odrzucenie użytkownika
    is_ajax3 = request.headers.get('X-Requested-With') == 'XMLHttpRequest3'
    if is_ajax3:
        if request.method == 'PUT':
            data = json.load(request)
            updated_values = data.get('formData')
            id=updated_values['id']

            user = User.objects.get(id=id)
            user.profile.is_user=updated_values['is_user']
            user.profile.is_operator=updated_values['is_operator']
            user.profile.is_admin=updated_values['is_admin']
            user.profile.operator=updated_values['operator']
            user.profile.approval=2
            user.save()

            return JsonResponse({'id':id,})
        return JsonResponse({'status': 'Invalid request'}, status=400) 
    return render(request, 'users_pages/admin.html',{'users':users,})    

#strona superadmina
@superadmin_required
def superuser(request):
    users = User.objects.all()

    #przekazanie niezatwierdzonych użytkowników
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            id = request.GET.get("id", None)
            if User.objects.filter(id = id).exists():
                user = User.objects.filter(id = id).values()
                profile=Profile.objects.filter(id = id).values()

                #pola do zmiany przy zatwierdzeniu/odrzuceniu
                user2 = User.objects.get(id=id)
                data={
                'is_user': user2.profile.is_user,
                'is_operator':user2.profile.is_operator,
                'is_admin': user2.profile.is_admin,
                'operator': user2.profile.operator,
                }
                form = ProfileForm_for_admin(initial=data,instance=user2)
                ctx = {}
                ctx.update(csrf(request))

                form_html = render_crispy_form(form, context=ctx)

                return JsonResponse({'context': list(chain(user,profile)),'form':form_html},safe=False)
        return JsonResponse({'status': 'Invalid request'}, status=400)
    

    #zatwierdzenie użytkownika
    is_ajax2 = request.headers.get('X-Requested-With') == 'XMLHttpRequest2'
    if is_ajax2:
        if request.method == 'PUT':
            data = json.load(request)
            updated_values = data.get('formData')
            id=updated_values['id']

            user = User.objects.get(id=id)
            user.profile.is_user=updated_values['is_user']
            user.profile.is_operator=updated_values['is_operator']
            user.profile.is_admin=updated_values['is_admin']
            user.profile.operator=updated_values['operator']
            user.profile.approval=1
            user.save()

            return JsonResponse({'id':id,})
        return JsonResponse({'status': 'Invalid request'}, status=400)


    #odrzucenie użytkownika
    is_ajax3 = request.headers.get('X-Requested-With') == 'XMLHttpRequest3'
    if is_ajax3:
        if request.method == 'PUT':
            data = json.load(request)
            updated_values = data.get('formData')
            id=updated_values['id']

            user = User.objects.get(id=id)
            user.profile.is_user=updated_values['is_user']
            user.profile.is_operator=updated_values['is_operator']
            user.profile.is_admin=updated_values['is_admin']
            user.profile.operator=updated_values['operator']
            user.profile.approval=2
            user.save()

            return JsonResponse({'id':id,})
        return JsonResponse({'status': 'Invalid request'}, status=400)    

    return render(request, 'users_pages/superadmin.html',{'users':users,})  

