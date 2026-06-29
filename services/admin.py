from django.contrib import admin

from .models import ServiceProvider


@admin.register(
ServiceProvider
)

class ProviderAdmin(

admin.ModelAdmin

):

    list_display=[

'full_name',

'service',

'approved'

    ]

    list_editable=[

'approved'

    ]
