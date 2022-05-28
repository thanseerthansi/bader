from django.urls import path
from .views import *

urlpatterns = [
   # path('propertytype/',PropertyTypeView.as_view()),
   path('property/',PropertyView.as_view()),
   path('propertyget/',PropertyGetView.as_view()),
   path('likedproperty/',LikedPropertyView.as_view()),
   path('images/',ImagesView.as_view()),
   path('recent/',RecentsearchedView.as_view()),
  

]