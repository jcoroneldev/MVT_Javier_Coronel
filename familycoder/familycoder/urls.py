from django.contrib import admin
from django.urls import path, include 
from familycoderapp.views import familia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('familycoderapp.urls')),
    path('familycoder/', include('familycoderapp.urls'))

]
