from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

# sprawdzenie, czy użytkownik jest użytkownikiem i ma zatwierdzone konto
def user_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/'):
    actual_decorator = user_passes_test(
        lambda u: u.profile.is_user and u.profile.approval == 1,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

# sprawdzenie, czy użytkownik jest operatorem i ma zatwierdzone konto
def operator_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/'):
    actual_decorator = user_passes_test(
        lambda u: u.profile.is_operator and u.profile.approval == 1,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


# sprawdzenie, czy użytkownik jest adminem i ma zatwierdzone konto
def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/'):
    actual_decorator = user_passes_test(
        lambda u: u.profile.is_admin and u.profile.approval == 1,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

 # sprawdzenie, czy użytkownik jest superadminem
def superadmin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/'):
    actual_decorator = user_passes_test(
        lambda u: u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator   