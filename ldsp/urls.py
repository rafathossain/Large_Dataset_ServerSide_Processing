from django.urls import path, include
from .views import *

urlpatterns = [
    # Table Page URL
    path('', ldsp, name='ldsp.home'),

    # Data Endpoint
    path('data/', ldspData, name='ldsp.data'),

    # Data Seed
    path('seed/', ldspSeed, name='ldsp.seed')
]
