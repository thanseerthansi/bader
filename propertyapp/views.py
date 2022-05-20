import json
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from propertyapp.models import PropertyTypesModel

from propertyapp.serializers import PropertyTypesSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class PropertyTypeView(ListAPIView):
    serializer_class = PropertyTypesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes =(IsAuthenticated,)

    def post(self,request):
        isadmin = self.request.user.is_admin
        superuser = self.request.user.is_superuser
        if isadmin==True or superuser == True:
            try:
                id = self.request.POST.get("id","")
               
                if id: 
                    if id.isdigit():
                        propertytype_qs = PropertyTypesModel.objects.filter(id=id)
                        if propertytype_qs.count():
                            propertytype_qs = propertytype_qs.first()
                            propertytype_obj = PropertyTypesSerializer(propertytype_qs,data=self.request.data,partial=True)
                            msg = "Successfully modified"
                        else: return Response({"Status":"False","Message":"No Records found with given id"})
                    else: return Response({"Status":False,"Message":"Provide valid id"}) 
                else: 
                    propertytype_obj = PropertyTypesSerializer(data=self.request.data,partial=True)
                    msg = "Successfully Created"
            
                propertytype_obj.is_valid(raise_exception=True)
                propertytype_obj.save()
                return Response({"Status":True,"Message":msg})
                

            except Exception as e: return Response({"Status":False,"Message":str(e),})
    def get_queryset(self):
        id = self.request.POST.get("id",'')
        type = self.request.POST.get("types","")
        qs = PropertyTypesModel.objects.all()
        if id : qs = qs.filter(id=id)
        if type : qs = qs.filter(types=type)
        return qs
    def delete(self,request):
        isadmin = self.request.user.is_admin
        superuser = self.request.user.is_superuser
        if isadmin == True or superuser == True:
            try:
               
                id = json.loads(id)
                objects = PropertyTypesModel.objects.filter(id__in=id)
                if objects.count():
                    objects.delete()
                    return Response({"Status":True,"Message":"deleted successfully"})
                else: return Response({"Status":False,"Message":"No records with given id" })
            except:
                return Response({
                    "Status" : False,
                    "Message" : "Something Went Wrong"
                })
        else:
            return Response({
                "Status" : False,
                "Message" : "Something Went Wrong"
            })
        