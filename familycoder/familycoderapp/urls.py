import imp
from django.urls import path
from familycoderapp.views import *

urlpatterns = [
    path('', familia, name="inicio"),
    path('familia/', familia, name="familia"), 
    ]
