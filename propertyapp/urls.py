from django.urls import path
from .views import *

urlpatterns = [
   path('propertytype/',PropertyTypeView.as_view()),
  

]