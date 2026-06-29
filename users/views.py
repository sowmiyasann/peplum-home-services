from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import login

from .models import User


def login_page(request):

    return render(
        request,
        'login.html'
    )


def register(request):

    if request.method=="POST":

        username=request.POST['username']

        email=request.POST['email']

        password=request.POST['password']

        role=request.POST['role']

        user=User.objects.create_user(

            username=username,

            email=email,

            password=password,

            role=role

        )

        login(
            request,
            user
        )

        if role=="provider":

            return redirect(
                '/provider-dashboard/'
            )

        return redirect(
            '/dashboard/'
        )

    return render(
        request,
        'register.html'
    )


def customer_dashboard(request):

    return render(
        request,
        'customer-dashboard.html'
    )


def provider_dashboard(request):

    return render(
        request,
        'provider-dashboard.html'
    )
