import json
# from math import sin, cos, sqrt, atan2, radians
# import math
# from django.db.models import When,Case,Sum
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
# from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.db.models.functions import GeometryDistance
from django.contrib.gis.geos import GEOSGeometry
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from badder.validation import Validate
from propertyapp.models import LikedPropertyModel, PropertyModel
from propertyapp.serializers import LikedPropertySerializer, PropertySerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from userapp.models import UserModel
# Create your views here.
# class PropertyTypeView(ListAPIView):
#     serializer_class = PropertyTypesSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes =(IsAuthenticated,)
#     def post(self,request):
#         isadmin = self.request.user.is_admin
#         isagent = self.request.user.is_agent
#         superuser = self.request.user.is_superuser
#         if isadmin==True or superuser == True or isagent==True:
#             try:
#                 id = self.request.POST.get("id","")              
#                 if id: 
#                     if id.isdigit():
#                         propertytype_qs = PropertyTypesModel.objects.filter(id=id)
#                         if propertytype_qs.count():
#                             propertytype_qs = propertytype_qs.first()
#                             propertytype_obj = PropertyTypesSerializer(propertytype_qs,data=self.request.data,partial=True)
#                             msg = "Successfully modified"
#                         else: return Response({"Status":"False","Message":"No Records found with given id"})
#                     else: return Response({"Status":False,"Message":"Provide valid id"}) 
#                 else: 
#                     propertytype_obj = PropertyTypesSerializer(data=self.request.data,partial=True)
#                     msg = "Successfully Created"           
#                 propertytype_obj.is_valid(raise_exception=True)
#                 propertytype_obj.save()
#                 return Response({"Status":True,"Message":msg})                
#             except Exception as e: return Response({"Status":False,"Message":str(e),})
#         else:return Response({"Status":False,"Message":"Something Went Wrong"})
#     def get_queryset(self):
#         try:
#             id = self.request.POST.get("id",'')
#             type = self.request.POST.get("types","")
#             qs = PropertyTypesModel.objects.all()
#             if id : qs = qs.filter(id=id)
#             if type : qs = qs.filter(types=type)
#             return qs
#         except :return None
#     # def get(self,request):
#     #     id = self.request.POST.get("id",'')
#     #     type = self.request.POST.get("types","")
#     #     qs = PropertyTypesModel.objects.all()
#     #     if id : qs = qs.filter(id=id)
#     #     if type : qs = qs.filter(types=type)
#     #     return Response({"data":PropertyTypesSerializer(qs,many=True).data})
    
#     def delete(self,request):
#         isadmin = self.request.user.is_admin
#         isagent = self.request.user.is_agent
#         superuser = self.request.user.is_superuser
#         if isadmin == True or superuser == True or isagent==True:
#             try:
#                 id = self.request.POST.get("id","[]")
#                 id = json.loads(id)
#                 objects = PropertyTypesModel.objects.filter(id__in=id)
#                 if objects.count():
#                     objects.delete()
#                     return Response({"Status":True,"Message":"deleted successfully"})
#                 else: return Response({"Status":False,"Message":"No records with given id" })
#             except Exception as e:
#                 return Response({
#                     "Status" : False,
#                     "Message" : str(e),
#                 })
#         else:
#             return Response({
#                 "Status" : False,
#                 "Message" : "Something Went Wrong"
#             })
class PropertyView(ListAPIView):
    serializer_class = PropertySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes =(IsAuthenticated,)
    # def get_queryset(self):
    #     try:
    #         id = self.request.POST.get("id",'')
    #         p_type = self.request.POST.get("property_type",'')
    #         city = self.request.POST.get("city",'')
    #         minimum_price = self.request.POST.get("price_minimum",'')
    #         maximum_price = self.request.POST.get("price_maximum",'')
    #         name = self.request.POST.get("name",'')
    #         p_radious = self.request.POST.get("radious",'')
    #         p_date = self.request.POST.get("date",'')
    #         p_purpose = self.request.POST.get('') 
    #         qs = PropertyModel.objects.all()
    #         if id:qs = qs.filter(id=id)
    #         if city:qs= qs.filter(property_city__icontains=city)
    #         if minimum_price:qs= qs.filter(property_price__gt=minimum_price)
    #         if maximum_price:qs= qs.filter(property_price__lt=maximum_price)
    #         if name:qs= qs.filter(property_name__icontains=name)
    #         if p_type:qs= qs.filter(property_type=p_type)
    #         if p_radious:qs= qs.filter(property_radious=p_radious)
    #         if p_date:qs= qs.filter(added_date=p_date)

    #         return qs
    #     except : return None
    def get(self,request):
        try:
            id = self.request.POST.get("id",'')
            p_type = self.request.POST.get("property_type",'')# eg residential , land....
            p_purpose = self.request.POST.get("property_purpose",'')
            city = self.request.POST.get("city",'')
            minimum_price = self.request.POST.get("price_minimum",'')
            maximum_price = self.request.POST.get("price_maximum",'')
            name = self.request.POST.get("name",'')
            residential_type = self.request.POST.get("residential_type",'')# eg villa or flat.... 
            p_radious = self.request.POST.get("radious",'')
            p_date = self.request.POST.get("date",'')
            latitude = self.request.POST.get("latitude")
            longitude = self.request.POST.get("longitude")
            distance = self.request.POST.get("distance",'')
            near_by = self.request.POST.get("near_by",'')
            room = self.request.POST.get("bedrooms",'')
            new = self.request.POST.get("new",'')           
            if near_by != "":
                mandatory = ['latitude','longitude','distance']
                data = Validate(self.request.data,mandatory)
                if data==True:
                    ref_location = GEOSGeometry(Point(float(longitude), float(latitude),srid=4326))               
                    print("dis",distance)
                    qs = PropertyModel.objects.filter(location__dwithin=(ref_location, D (km=distance))) \
                    .annotate(distance=GeometryDistance('location', ref_location)) \
                    .order_by("distance")
                    # print(queryset)
                    # qs = queryset
                else:return Response({"Status":False,"Message":data})
            else:
                qs = PropertyModel.objects.all()
            if id:qs = qs.filter(id=id)
            if city:qs= qs.filter(property_city__icontains=city)
            if minimum_price:qs= qs.filter(property_price__gt=minimum_price)
            if maximum_price:qs= qs.filter(property_price__lt=maximum_price)
            if name:qs= qs.filter(property_name__icontains=name)
            if residential_type:qs= qs.filter(residential_type__icontains=residential_type)# eg villa or flat 
            if p_type:qs= qs.filter(property_type__icontains=p_type)
            if p_purpose:qs= qs.filter(property_purpose=p_purpose)
            if p_radious:qs= qs.filter(property_radious=p_radious)
            if room:qs = qs.filter(property_room=room)
            if p_date:qs= qs.filter(added_date=p_date)
            if new != "": qs = qs.order_by('-id')
            else: qs = qs.order_by('id')
            return Response({"data":PropertySerializer(qs,many=True).data})
        except Exception as e: return Response({"Status":False,"Message":str(e)})    

    def post(self,request):
        isadmin = self.request.user.is_admin
        isagent = self.request.user.is_agent
        userid = self.request.user.id
        superuser = self.request.user.is_superuser
        if isadmin==True or superuser == True or isagent==True:
            mandatory = ['latitude','longitude']
            data = Validate(self.request.data,mandatory)
            id = self.request.POST.get("id",'')
            lat = self.request.POST.get("latitude","")
            lon = self.request.POST.get("longitude","")        
            try:            
                if userid:
                    user_qs = UserModel.objects.filter(id=userid)
                    if user_qs.count():
                        user_qs = user_qs.first()
                    else:return Response({"Status":False,"Messsage":"User not found"})                  
                # if property_typeid:
                #     property_type_qs = PropertyTypesModel.objects.filter(id=property_typeid)
                #     print("proptypeqs",property_type_qs)
                #     if property_type_qs.count():
                #         property_type_qs = property_type_qs.first()
                #         print("proptypeqs",property_type_qs)
                    # else: return Response({"Status":False,"Meassage":"Property type not found with given id"})
                if id:
                    if id.isdigit():                       
                        property_qs = PropertyModel.objects.filter(id=id)
                        if property_qs.count(): 
                            property_qs = property_qs.first()
                            # if not property_typeid: property_type_qs = property_qs.property_type
                            # print("sgr",property_type_qs)
                            property_obj = PropertySerializer(property_qs,data=self.request.data,partial=True)
                            msg = "Successfully updated"

                        else:return Response({"Status":False,"Message":"No Record found with given id"})
                    else: return Response({"Status":False,"Message":"Provide valid id"})
                else:
                    if data == True:
                        property_obj = PropertySerializer(data=self.request.data,partial=True)
                        msg = "Successfully Created"
                    else:return Response({"Status":False,"Message":data})
                location =GEOSGeometry(Point(float(lon), float(lat),srid=4326))
                print("loaction",location)
                property_obj.is_valid(raise_exception=True)
                property_obj.save(agent=user_qs,location=location)
                return Response({"Status":True,"Message":msg})
            except Exception as e: return Response({"Status":False,"Message":str(e)}) 
        else: return Response({"Status":False,"Message":"Signup as agent"})
            
    def delete(self,request):
        isadmin = self.request.user.is_admin
        isagent = self.request.user.is_agent
        superuser = self.request.user.is_superuser
        if isadmin == True or superuser == True or isagent==True:
            try:
                id = self.request.POST.get("id","[]")
                id = json.loads(id)
                objects = PropertyModel.objects.filter(id__in=id)
                if objects.count():
                    objects.delete()
                    return Response({"Status":True,"Message":"deleted successfully"})
                else: return Response({"Status":False,"Message":"No records with given id" })
            except Exception as e:
                return Response({
                    "Status" : False,
                    "Message" : str(e),
                })
        else:
            return Response({
                "Status" : False,
                "Message" : "Something Went Wrong"
            })
            

class PropertyGetView(ListAPIView):
    def get(self,request):
        try:
            id = self.request.POST.get("id",'')
            p_type = self.request.POST.get("property_type",'')
            p_purpose = self.request.POST.get("property_purpose",'')
            city = self.request.POST.get("city",'')
            residential_type = self.request.POST.get("residential_type",'')# eg villa or flat.... 
            minimum_price = self.request.POST.get("price_minimum",'')
            maximum_price = self.request.POST.get("price_maximum",'')
            name = self.request.POST.get("name",'')
            p_radious = self.request.POST.get("radious",'')
            p_date = self.request.POST.get("date",'')
            dont_show = self.request.POST.get("exclude",'')
            latitude = self.request.POST.get("latitude")
            longitude = self.request.POST.get("longitude")
            distance = self.request.POST.get("distance",'')
            near_by = self.request.POST.get("near_by",'')
            room = self.request.POST.get("bedrooms",'')
            new = self.request.POST.get("new",'')          
            if near_by != "":
                mandatory = ['latitude','longitude','distance']
                data = Validate(self.request.data,mandatory)
                if data==True:
                    ref_location = GEOSGeometry(Point(float(longitude), float(latitude),srid=4326))               
                    print("dis",distance)
                    qs = PropertyModel.objects.filter(location__dwithin=(ref_location, D (km=distance))) \
                    .annotate(distance=GeometryDistance('location', ref_location)) \
                    .order_by("distance")
                    # print(queryset)
                    # qs = queryset
                else:return Response({"Status":False,"Message":data})
            else:
                qs = PropertyModel.objects.all()
            if id:qs = qs.filter(id=id)
            if city:qs= qs.filter(property_city__icontains=city)
            if minimum_price:qs= qs.filter(property_price__gt=minimum_price)
            if maximum_price:qs= qs.filter(property_price__lt=maximum_price)
            if name:qs= qs.filter(property_name__icontains=name)
            if residential_type:qs= qs.filter(residential_type__icontains=residential_type)# eg villa or flat 
            if p_type:qs= qs.filter(property_type__icontains=p_type)
            if p_radious:qs= qs.filter(property_radious=p_radious)
            if p_date:qs= qs.filter(added_date=p_date)
            if room:qs = qs.filter(property_room=room)
            if p_purpose:qs= qs.filter(property_purpose=p_purpose)
            if dont_show : qs = qs.exclude(property_type__icontains=dont_show)
            if new != "": qs = qs.order_by('-id')
            else: qs = qs.order_by('id')
            return Response({"data":PropertySerializer(qs ,many=True).data})
        except Exception as e: return Response({"Status":False,"Message":str(e)})

# class checkquery(ListAPIView):
#     def get(self,request):       
#         latitude = self.request.POST.get("latitude")
#         longitude = self.request.POST.get("longitude")
#         distance = self.request.POST.get("distance",'')
#         near_by = self.request.POST.get("near_by",'')
#         id = self.request.POST.get("id",'')
#         # longitude = self.request.query_params["longitude"]
#         # print("lat",latitude)
#         # print("lon",longitude)
#         # print(type(longitude))
#         if near_by != "":
#             ref_location = GEOSGeometry(Point(float(longitude), float(latitude),srid=4326))
            
#             print("dis",distance)
#             queryset = PropertyModel.objects.filter(location__dwithin=(ref_location, D (km=distance))) \
#             .annotate(distance=GeometryDistance('location', ref_location)) \
#             .order_by("distance")
#             print(queryset)
#             qs = queryset
#         else: qs =PropertyModel.objects.all()
#         if id: qs= qs.filter(id=id)
            
#         return Response({"data":PropertySerializer(qs ,many=True).data})

class LikedPropertyView(ListAPIView):
    serializer_class = LikedPropertySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes =(AllowAny,)
    def get_queryset(self):
        try:
            userid = self.request.user.id
            id = self.request.POST.get("id",'')
            property_id = self.request.POST.get("property")
            qs = LikedPropertyModel.objects.all()
            if id:qs = qs.filter(id=id)
            else: qs = qs.filter(user_id=userid)
            if property_id:qs = qs.filter(liked_property_id=id)
            return qs
        except : return None
   
    # def post(self,request):
    #   userid = self.request.user.id
    #                 print("userid",userid)  
    #                 try:
    #                     if userid:
    #                         user_qs = UserModel.objects.filter(id=userid)
    #                         if user_qs.count():
    #                             user_qs = user_qs.first()
    #                             user_obj = LikedPropertyModel.objects.create(user=user_qs)
    #                             return Response({"Status":True,"Message":"Successfully created"})

    #                         else:return Response({"Status":False,"Message":"No user found "})
    #                     else: return Response({|"Status":False,"Message":"Went Wrong"})
    #                 except Exception as e: return Response({"Status":False,"Message":str(e)})
    
    def patch(self,request):
        try:
            userid = self.request.user.id
            likedpropertyid = self.request.POST['property']
            keyword = self.request.POST['keyword']
            if userid:
                user_qs = UserModel.objects.filter(id=userid)
                if user_qs.count():
                    user_qs = user_qs.first()
                    print("userqs",user_qs)
                    likedproperty_qs = LikedPropertyModel.objects.filter(user=user_qs)
                    if likedproperty_qs.count()==0 :LikedPropertyModel.objects.create(user=user_qs)
                if likedproperty_qs.count(): likedproperty_obj=likedproperty_qs.first()
                else:return Response({"Status":False,"Message":"Went wrong"}) 
                property_qs = PropertyModel.objects.filter(id=likedpropertyid)
                if property_qs.count(): property_obj = property_qs.first()
                else: 
                    return Response({"status":False,"message":"property not found"})
                if keyword=="add":
                    likedproperty_obj.liked_property.add(property_obj)
                    msg = "type added successfully"
                if keyword=="remove":
                    likedproperty_obj.liked_property.remove(property_obj)
                    msg = "type removed successfully"
                return Response({
                    "status":True,
                    "message":msg,
                })
            else:return Response({"Status":False,"Message":"You Need to Login "})
        except Exception as e:
            return Response({"status":False,"msg": str(e),})       
    def delete(self,request):
        try:
            userid = self.request.user.id
            id = self.request.POST.get("id","[]")
            id = json.loads(id)
            objects = LikedPropertyModel.objects.filter(user_id=userid,id__in=id)
            if objects.count():
                objects.delete()
                return Response({"Status":True,"Message":"deleted successfully"})
            else: return Response({"Status":False,"Message":"No records with given id" })
        except Exception as e:
            return Response({
                "Status" : False,
                "Message" : str(e),
            })