# Created by Miguel Angel Aguilar 
# maac35@gmail.com - nov 2019

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def super_user_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='sign_in'):

    actual_decorator = user_passes_test(
        lambda u: u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator