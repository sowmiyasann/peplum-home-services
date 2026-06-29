from django.urls import path

from .views import *


urlpatterns=[

path(
'login/',
login_page
),

path(
'register/',
register
),

path(
'dashboard/',
customer_dashboard
),

path(
'provider-dashboard/',
provider_dashboard
),

]
