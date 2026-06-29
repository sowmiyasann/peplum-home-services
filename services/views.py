from django.shortcuts import render
from django.shortcuts import redirect

from .models import ServiceProvider


def home(request):

    return render(
        request,
        'index.html'
    )


def provider_register(request):

    if request.method=="POST":

        ServiceProvider.objects.create(

            full_name=request.POST['name'],

            email=request.POST['email'],

            phone=request.POST['phone'],

            service=request.POST['service'],

            experience=request.POST['experience'],

            location=request.POST['location']

        )

        return redirect(
            '/provider-dashboard/'
        )

    return render(
        request,
        'provider-register.html'
    )
