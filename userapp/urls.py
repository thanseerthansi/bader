from django.urls import path
from .views import *

urlpatterns = [
   path('login/',LoginView.as_view()),
   path('user/',UserView.as_view()),
   path('logout/',Logout.as_view()),
   path('whoami/',WhoAmI.as_view()),

]