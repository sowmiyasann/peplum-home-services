from django.db import models


class ServiceProvider(models.Model):

    SERVICE=[

('mechanic','Mechanic'),

('plumber','Plumber'),

('electrician','Electrician'),

('cleaning','Cleaning'),

('cooking','Cooking')

]

    full_name=models.CharField(
        max_length=100
    )

    email=models.EmailField()

    phone=models.CharField(
        max_length=20
    )

    service=models.CharField(
        max_length=50,
        choices=SERVICE
    )

    experience=models.IntegerField()

    location=models.CharField(
        max_length=100
    )

    available=models.BooleanField(
        default=True
    )

    approved=models.BooleanField(
        default=False
    )

    def __str__(self):

        return self.full_name
