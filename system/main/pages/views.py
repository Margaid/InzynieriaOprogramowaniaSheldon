from django.shortcuts import render, redirect
from .decorators import user_required, operator_required, admin_required, superadmin_required
from django.contrib.auth.models import User
from register.models import Profile
from .forms import ProfileForm_for_super_admin, ProfileForm_for_admin, ReservationForm_for_user, ReservationForm_for_operator, ReservationDataBase, Form_for_approval_buttons_reservations_superadmin, Form_for_approval_buttons_reservations_admin
from .models import LAB_STATIONS, ReservationDataBase
from django.http import JsonResponse
import json
from itertools import chain
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form


# wybranie strony w zależności od rodzaju użytkownika
def page(request):
    user = request.user
    if user.profile.is_user and user.is_authenticated:
        return redirect('user/')
    elif user.profile.is_operator and user.is_authenticated:
        return redirect('operator/')
    elif user.profile.is_admin and user.is_authenticated:
        return redirect('admin/')
    elif user.is_superuser and user.is_authenticated:
        return redirect('superuser/')
    else:
        # tu dać stronę 404 albo żeby się zalogować
        return render(request, 'base/base.html')

# strona użytkownika


@user_required
def user(request):
    reservations = ReservationDataBase.objects.all()
    stations= [c[1] for c in LAB_STATIONS]

    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            lab = request.GET.get("lab", None)
            if lab in stations:
                # pola do zmiany przy zatwierdzeniu/odrzuceniu
               # user2 = User.objects.get(id=id)
                data = {
                    'lab_station': lab,
                }
                form = ReservationForm_for_user(initial=data, instance=request.user)
                ctx = {}
                ctx.update(csrf(request))

                form_html = render_crispy_form(form, context=ctx)
                return JsonResponse({'form': form_html,'lab':lab})
        return JsonResponse({'status': 'Invalid request'}, status=400)

    # przesłanie rezerwacji
    is_ajax2 = request.headers.get('X-Requested-With') == 'XMLHttpRequest2'
    if is_ajax2:
        if request.method == 'PUT':
            data = json.load(request)
            form_values = data.get('formData')
            lab = [c[0] for c in LAB_STATIONS if c[1]==form_values['lab_station']][0]
            #uzupełnianie danych rezerwacji
            reservation=ReservationDataBase()
            reservation.user=request.user
            reservation.lab_station=lab
            reservation.start_date=form_values['start_date']
            reservation.end_date=form_values['end_date']
            reservation.operator=form_values['operator']
            reservation.save()
            return JsonResponse({'lab': lab, })
        return JsonResponse({'status': 'Invalid request'}, status=400)


    if request.method == 'POST':
        form = ReservationForm_for_user(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
    else:
        form = ReservationForm_for_user()
    return render(request, 'users_pages/user.html', {'form': form,'reservations':reservations,'stations':stations})


# strona operatora
@operator_required
def operator(request):
    reservations = ReservationDataBase.objects.all()

     # pokazywanie more info o rezerwacjach
    is_ajax4 = request.headers.get('X-Requested-With') == 'XMLHttpRequest4'
    if is_ajax4:
        if request.method == 'GET':
            id = request.GET.get("id", None)
            if ReservationDataBase.objects.filter(reservation_id=id).exists():

                reservations2 = ReservationDataBase.objects.get(
                    reservation_id=id)
                reservations = ReservationDataBase.objects.filter(
                    reservation_id=id).values()
                user = User.objects.filter(
                    id=reservations2.user_id).values()
                profile = Profile.objects.filter(
                    id=reservations2.user_id).values()

                data = {
                    'reservation_id': id,
                }

                form = Form_for_approval_buttons_reservations_superadmin(
                    initial=data)

                ctx = {}
                ctx.update(csrf(request))

                form_html = render_crispy_form(form, context=ctx)

                return JsonResponse({'context': list(reservations), 'user': list(chain(user, profile)), 'form': form_html})
        return JsonResponse({'status': 'Invalid request'}, status=400)

    is_ajax5 = request.headers.get('X-Requested-With') == 'XMLHttpRequest5'
    if is_ajax5:
        if request.method == 'PUT':
            data = json.load(request)
            id = data.get('id')
            reservations = ReservationDataBase.objects.get(reservation_id=id)
            reservations.approved_status_operator = 1
            reservations.save()

            return JsonResponse({'id': id, })
        return JsonResponse({'status': 'Invalid request'}, status=400)
 # odrzucenie rezerwacji
    is_ajax6 = request.headers.get('X-Requested-With') == 'XMLHttpRequest6'
    if is_ajax6:
        if request.method == 'PUT':
            data = json.load(request)
            id = data.get('id')
            reservations = ReservationDataBase.objects.get(reservation_id=id)
            reservations.approved_status_operator = 2
            reservations.save()

            return JsonResponse({'id': id, })
        return JsonResponse({'status': 'Invalid request'}, status=400)

    # if response.method == 'POST':
    #     form = ReservationForm_for_operator(response.POST)
    #     if form.is_valid():
    #         reservation = form.save(commit=False)
    #         reservation.user = response.user
    #         reservation.save()
    # else:
    #     form = ReservationForm_for_operator()
    return render(request, 'users_pages/operator.html', {'reservations': reservations})

# strona admina


@admin_required
def admin(request):
    users = User.objects.all()
    reservations = ReservationDataBase.objects.all()

    # przekazanie niezatwierdzonych użytkowników
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            id = request.GET.get("id", None)
            if User.objects.filter(id=id).exists():
                user = User.objects.filter(id=id).values()
                profile = Profile.objects.filter(id=id).values()

                # pola do zmiany przy zatwierdzeniu/odrzuceniu
                user2 = User.objects.get(id=id)
                data = {
                    'is_user': user2.profile.is_user,
                    'is_operator': user2.profile.is_operator,
                    'is_admin': user2.profile.is_admin,
                    'operator': user2.profile.operator,
                }
                form = ProfileForm_for_admin(initial=data, instance=user2)
                ctx = {}
                ctx.update(csrf(request))

                form_html = render_crispy_form(form, context=ctx)

                return JsonResponse({'context': list(chain(user, profile)), 'form': form_html}, safe=False)
        return JsonResponse({'status': 'Invalid request'}, status=400)

    # zatwierdzenie użytkownika
    is_ajax2 = request.headers.get('X-Requested-With') == 'XMLHttpRequest2'
    if is_ajax2:
        if request.method == 'PUT':
            data = json.load(request)
            updated_values = data.get('formData')
            id = updated_values['id']

            user = User.objects.get(id=id)
            user.profile.is_user = updated_values['is_user']
            user.profile.is_operator = updated_values['is_operator']
            user.profile.is_admin = updated_values['is_admin']
            user.profile.operator = updated_values['operator']
            user.profile.approval = 1
            user.save()

            return JsonResponse({'id': id, })
        return JsonResponse({'status': 'Invalid request'}, status=400)

    # odrzucenie użytkownika
    is_ajax3 = request.headers.get('X-Requested-With') == 'XMLHttpRequest3'
    if is_ajax3:
        if request.method == 'PUT':
            data = json.load(request)
            updated_values = data.get('formData')
            id = updated_values['id']

            user = User.objects.get(id=id)
            user.profile.is_user = updated_values['is_user']
            user.profile.is_operator = updated_values['is_operator']
            user.profile.is_admin = updated_values['is_admin']
            user.profile.operator = updated_values['operator']
            user.profile.approval = 2
            user.save()

            return JsonResponse({'id': id, })
        return JsonResponse({'status': 'Invalid request'}, status=400)

    # pokazywanie more info o rezerwacjach
    is_ajax4 = request.headers.get('X-Requested-With') == 'XMLHttpRequest4'
    if is_ajax4:
        if request.method == 'GET':
            id = request.GET.get("id", None)
            if ReservationDataBase.objects.filter(reservation_id=id).exists():

                reservations2 = ReservationDataBase.objects.get(
                    reservation_id=id)
                reservations = ReservationDataBase.objects.filter(
                    reservation_id=id).values()
                user = User.objects.filter(
                    id=reservations2.user_id).values()
                profile = Profile.objects.filter(
                    id=reservations2.user_id).values()

                data = {
                    'reservation_id': id,
                }

                form = Form_for_approval_buttons_reservations_admin(
                    initial=data)

                ctx = {}
                ctx.update(csrf(request))

                form_html = render_crispy_form(form, context=ctx)

                return JsonResponse({'context': list(reservations), 'user': list(chain(user, profile)), 'form': form_html})
        return JsonResponse({'status': 'Invalid request'}, status=400)


    # odrzucenie rezerwacji
    is_ajax6 = request.headers.get('X-Requested-With') == 'XMLHttpRequest6'
    if is_ajax6:
        if request.method == 'PUT':
            data = json.load(request)
            id = data.get('id')
            reservations = ReservationDataBase.objects.get(reservation_id=id)
            reservations.approved_status = 2
            reservations.save()

            return JsonResponse({'id': id, })
        return JsonResponse({'status': 'Invalid request'}, status=400)


    return render(request, 'users_pages/admin.html', {'users': users, 'reservations':reservations})



# strona superadmina
@superadmin_required
def superuser(request):
    users = User.objects.all()
    reservations = ReservationDataBase.objects.all()
    # przekazanie niezatwierdzonych użytkowników
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            id = request.GET.get("id", None)
            if User.objects.filter(id=id).exists():
                user = User.objects.filter(id=id).values()
                profile = Profile.objects.filter(id=id).values()

                # pola do zmiany przy zatwierdzeniu/odrzuceniu
                user2 = User.objects.get(id=id)
                data = {
                    'is_user': user2.profile.is_user,
                    'is_operator': user2.profile.is_operator,
                    'is_admin': user2.profile.is_admin,
                    'operator': user2.profile.operator,
                }
                form = ProfileForm_for_super_admin(
                    initial=data, instance=user2)
                ctx = {}
                ctx.update(csrf(request))

                form_html = render_crispy_form(form, context=ctx)

                return JsonResponse({'context': list(chain(user, profile)), 'form': form_html}, safe=False)
        return JsonResponse({'status': 'Invalid request'}, status=400)

    # zatwierdzenie użytkownika
    is_ajax2 = request.headers.get('X-Requested-With') == 'XMLHttpRequest2'
    if is_ajax2:
        if request.method == 'PUT':
            data = json.load(request)
            updated_values = data.get('formData')
            id = updated_values['id']

            user = User.objects.get(id=id)
            user.profile.is_user = updated_values['is_user']
            user.profile.is_operator = updated_values['is_operator']
            user.profile.is_admin = updated_values['is_admin']
            user.profile.operator = updated_values['operator']
            user.profile.approval = 1
            user.save()

            return JsonResponse({'id': id, })
        return JsonResponse({'status': 'Invalid request'}, status=400)

    # odrzucenie użytkownika
    is_ajax3 = request.headers.get('X-Requested-With') == 'XMLHttpRequest3'
    if is_ajax3:
        if request.method == 'PUT':
            data = json.load(request)
            updated_values = data.get('formData')
            id = updated_values['id']

            user = User.objects.get(id=id)
            user.profile.is_user = updated_values['is_user']
            user.profile.is_operator = updated_values['is_operator']
            user.profile.is_admin = updated_values['is_admin']
            user.profile.operator = updated_values['operator']
            user.profile.approval = 2
            user.save()

            return JsonResponse({'id': id, })
        return JsonResponse({'status': 'Invalid request'}, status=400)

    # pokazywanie more info o rezerwacjach
    is_ajax4 = request.headers.get('X-Requested-With') == 'XMLHttpRequest4'
    if is_ajax4:
        if request.method == 'GET':
            id = request.GET.get("id", None)
            if ReservationDataBase.objects.filter(reservation_id=id).exists():

                reservations2 = ReservationDataBase.objects.get(
                    reservation_id=id)
                reservations = ReservationDataBase.objects.filter(
                    reservation_id=id).values()
                user = User.objects.filter(
                    id=reservations2.user_id).values()
                profile = Profile.objects.filter(
                    id=reservations2.user_id).values()

                data = {
                    'reservation_id': id,
                }

                form = Form_for_approval_buttons_reservations_superadmin(
                    initial=data)

                ctx = {}
                ctx.update(csrf(request))

                form_html = render_crispy_form(form, context=ctx)

                return JsonResponse({'context': list(reservations), 'user': list(chain(user, profile)), 'form': form_html})
        return JsonResponse({'status': 'Invalid request'}, status=400)

   # zatwierdzenie rezerwacji
    is_ajax5 = request.headers.get('X-Requested-With') == 'XMLHttpRequest5'
    if is_ajax5:
        if request.method == 'PUT':
            data = json.load(request)
            id = data.get('id')
            reservations = ReservationDataBase.objects.get(reservation_id=id)
            reservations.approved_status = 1
            reservations.save()

            return JsonResponse({'id': id, })
        return JsonResponse({'status': 'Invalid request'}, status=400)

    # odrzucenie rezerwacji
    is_ajax6 = request.headers.get('X-Requested-With') == 'XMLHttpRequest6'
    if is_ajax6:
        if request.method == 'PUT':
            data = json.load(request)
            id = data.get('id')
            reservations = ReservationDataBase.objects.get(reservation_id=id)
            reservations.approved_status = 2
            reservations.save()

            return JsonResponse({'id': id, })
        return JsonResponse({'status': 'Invalid request'}, status=400)

    return render(request, 'users_pages/superadmin.html', {'users': users, 'reservations': reservations})
