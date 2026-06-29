from django.db import models


class ServiceProvider(
models.Model
):

    SERVICE=[

('mechanic','Mechanic'),

('plumber','Plumber'),

('electrician','Electrician'),

('cleaning','Cleaning'),

('cooking','Cooking')

]

    name=models.CharField(
        max_length=100
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

    profile=models.ImageField(
        upload_to='providers'
    )
