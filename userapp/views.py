import json
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from userapp.models import UserModel

from userapp.serializers import UserSerializer
from badder.validation import Validate

# Create your views here.
class UserView(ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes =(AllowAny,)
    
    def get_queryset(self):
        try:
            id = self.request.POST.get("id",'')
            isagent = self.request.POST.get("is_agent",'')#make agent  True to filter the agents 
            isadmin = self.request.POST.get("is_admin",'')#make agent  True to filter the agents 
            qs = UserModel.objects.all()
            if id: qs= qs.filter(id=id)
            if isagent: qs = qs.filter(is_agent=isagent)
            if isadmin: qs = qs.filter(is_admin=isadmin)
            return qs.order_by('-id')
        except :
            return None

    def post(self,request):
        userobj = ""
        # isadmin = self.request.user.is_admin
        # superuser = self.request.user.is_superuser
        # if isadmin==True or superuser == True:
        id = self.request.POST.get("id","")
        if id:
            if id.isdigit():
                try:
                    user = UserModel.objects.filter(id=id)
                    if user.count():
                        user = user.first()
                    else:return Response({"Status":False,"Message":"User not found"})
                    serializer = UserSerializer(user,data=request.data,partial= True)
                    serializer.is_valid(raise_exception=True)

                    password =  self.request.POST.get('password','')
                    if password:
                        msg = "user details and Password updated successfully"
                        user_obj = serializer.save(password = make_password(password))
                    else: 
                        msg = "User details updated successfully"
                        user_obj = serializer.save()
                    datas = Token.objects.filter(user = id)
                    if datas.count(): datas.delete()
                    else: pass
                  
                    return Response({"Status":True,"Message":msg})
                except Exception as e:
                    # print(f"Exception occured{e}")
                    if  user_obj : user_obj.delete()
                    else : pass
                    return  Response({
                        "Status":False,
                        "Message":f"Excepction occured {e}"
                    })
            else: return Response({"Status":False,"Message":"Please provide valid user"})
        else:
            mandatory = ['username','email','password',]
            data = Validate(self.request.data,mandatory)
            if data == True:
                try:
                    serializer = UserSerializer(data=request.data, partial=True)
                    serializer.is_valid(raise_exception=True)
                
                    msg = "Created New User"
                    user_obj = serializer.save(password=make_password(self.request.data['password']))
                    return Response({"Status":True,"Message":msg})
                except Exception as e :
                    return Response({"Status":False,"Message":str(e),})
            else : return Response({"Status":False,"Message":data})
        # else:return Response({"Status":False,"Message":"Something went wrong"})
    def delete(self,request):
        # isadmin = self.request.user.is_admin
        # superuser = self.request.user.is_superuser
        # if isadmin==True or superuser == True:
        try:
            id = self.request.POST.get('id','')
            u_obj = UserModel.objects.filter(id=id)
            if u_obj.count():
                print("obj",u_obj)
                u_obj.delete()
        
                return Response({"status":True,"message":"deleted successfully"})
            else: return Response({"status":False,"message":"No records with given id" })
            
        except Exception as e:
            return Response({"status":False,"message":str(e),})
        # else: return Response({"Status":False,"Message":"Something went wrong"})
            
class WhoAmI(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self,request):
        try:
            return Response({
                "Status":1,
                "Data":self.request.user.username
            })
        except Exception as e: return Response({"Status":False,"Message":str(e),})


        
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        # print(serializer)
        try:
            test = serializer.is_valid(raise_exception=True) 
            user = serializer.validated_data['user']


            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "STATUS":True,
                'token': "Token "+token.key,
                'user_id': user.pk,
                'username': user.username,
                'is_superuser':user.is_superuser,
            })
        except Exception as e:
            return Response({
                "STATUS":False,
                "MESSAGE":"Incorrect Username or Password",
                "excepction":str(e),
            })
class Logout(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
  
    def get(self,request):
        try:
            Data = Token.objects.get(user = self.request.user.id)
            Data.delete()
            return Response({"status":True,"message":"logout successfully"})
        except Exception as e: return Response({"Status":False,"Message":str(e)})
