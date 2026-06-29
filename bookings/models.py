from django.db import models


class Booking(
models.Model
):

    STATUS=[

('pending','Pending'),

('accepted','Accepted'),

('completed','Completed')

]

    customer=models.CharField(
        max_length=100
    )

    provider=models.CharField(
        max_length=100
    )

    date=models.DateField()

    time=models.TimeField()

    payment=models.BooleanField(
        default=False
    )

    status=models.CharField(
        max_length=50,
        choices=STATUS
    )
