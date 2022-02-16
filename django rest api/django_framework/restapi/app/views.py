from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Contact
from .serializers import ContactModelSerializer,ContactSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
#Creating Basic Class
@csrf_exempt
def contact_list(request):
    if request.method == 'GET':
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact,many=True)
        return JsonResponse(serializer.data,safe =False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ContactSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        return JsonResponse(serializer.errors,status = 400)

@csrf_exempt
def contact_desc(request,pk):
    try:
        contact = Contact.objects.all(pk = pk)
    except:
        return HttpResponse(status = 404)
    if request.method == 'GET':
        serializer = ContactSerializer(contact)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(contact)
        serializer = ContactSerializer(contact,data =data)
        if serializer.is_valid():
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status = 400)
    elif request.method == 'DELETE':
        contact.delete()
        return HttpResponse(status = 204)

#function based api view
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
@api_view(['GET','POST'])
def contact_api_view(request):
    if request.method == 'GET':
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact,many = True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = ContactSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def contact_op_api_view(request,pk):
    try:
        contact = Contact.objects.all(pk=pk)
    except:
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        serializer = ContactSerializer(contact)
        return Response(serializer.data)
    elif request.method =='GET':
        serializer = ContactSerializer(contact,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    elif request.method =='GET':
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



