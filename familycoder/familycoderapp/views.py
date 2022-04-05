import imp
import re
from django.http import HttpResponse
from django.shortcuts import render
from familycoderapp.models import *


# Create your views here.

def familia(request):
     try:
          data = request.GET['nombre']
          print (type(data))
          if data:
               familiar1 = familiar.objects.get( nombre = data )
               print (type(familiar1))
               return render(request,"familycoderapp/base.html", {"familiar": familiar1[0]})
     except:
          return render(request,"familycoderapp/base.html")
    
