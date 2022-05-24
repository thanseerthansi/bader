from django.urls import path
from .views import *

urlpatterns = [
   path('propertytype/',PropertyTypeView.as_view()),
   path('property/',PropertyView.as_view()),
   path('propertyget/',PropertyGetView.as_view()),
   path('likedproperty/',LikedPropertyView.as_view()),
   # path('querycheck/',checkquery.as_view()),
  

]