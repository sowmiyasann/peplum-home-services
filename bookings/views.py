from django.shortcuts import render
from django.shortcuts import redirect

from .models import Booking


def services_page(request):

    return render(
        request,
        'services.html'
    )


def booking(request):

    if request.method=="POST":

        customer=request.POST['customer']

        provider=request.POST['provider']

        date=request.POST['date']

        time=request.POST['time']

        Booking.objects.create(

            customer=customer,

            provider=provider,

            date=date,

            time=time,

            payment=False,

            status='pending'

        )

        return redirect(
            '/dashboard/'
        )

    return render(
        request,
        'booking.html'
    )
