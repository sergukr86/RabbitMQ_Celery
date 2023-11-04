from django.urls import path
from sms.views import main, thanks

urlpatterns = [
    path("", main, name="main"),
    path("thanks/", thanks, name="thanks")
               ]
