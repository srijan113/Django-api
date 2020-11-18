from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from django.http import HttpResponse,JsonResponse



from rest_framework.decorators import api_view,APIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.



# if we dont use api_view as decorator then we have to use JSONParser.parse() to get the json data form url 
@api_view(['GET','POST'])
def apiListView(request):
    if request.method=="GET":
        book=Book.objects.all()
        serializer=BookSerializer(book,many=True)
        return Response(serializer.data)

    elif request.method=="POST":
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#if you are using api views then you have use auhentication like following wise.But they are not working not sure why?
@api_view(['GET','PUT','DELETE'])
# @authentication_classes([SessionAuthentication,BasicAuthentication])
# @permission_classes([IsAuthenticated])
def apiDetailView(request,pk):
    try:
        book=Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse('404 Error')
    
    if request.method=='GET':
        serializer=BookSerializer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)
 
    elif request.method=="PUT":
        serializer=BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#this is your class based api views which is simple then function view just modification are limited
class apiClassListView(APIView):

    def get(self,request):
        book=Book.objects.all()
        serializer=BookSerializer(book,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class apiClassDetailView(APIView):

    def get_object(self,pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
        book=self.get_object(pk)
        serializer=BookSerializer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        book=self.get_object(pk)
        serializer=BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        book=self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#this is the generic view if this is suitable we can always use above method of function and class to get api for our project

#if you are using any class views then you can use like authenticted_class=[] for the authentication.
class apiGenericListView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=BookSerializer
    queryset=Book.objects.all()

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)


class apiGenericDetailView(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=BookSerializer
    authenticated_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Book.objects.all()
    lookup_field='pk'

    def get(self,request,pk):
        if pk:
            return self.retrieve(request,pk)
        else:
            return self.list(request)

    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)