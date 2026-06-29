from django.contrib import admin

from django.urls import path

from django.urls import include

from services.views import home


urlpatterns=[

path(
'admin/',
admin.site.urls
),

path(
'',
home
),

path(
'',
include(
'users.urls'
)
),

path(
'',
include(
'bookings.urls'
)
),

]
