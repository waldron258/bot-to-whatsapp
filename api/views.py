from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Customer_Information

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomerSerializer

# Twilio stuff
import os
from twilio.rest import Client
# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
# End Twilio stuff

# Create your views here.

@api_view(['GET'])
def getInformation(request):
    api_urls = {
        'List':'/customer-list/',
        'Detail View':'/customer-detarequestil/<str:pk>/',
        'Create':'/customer-create/',
        'Update':'/customer-update/<str:pk>/',
        'Delete':'/customer-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def customerList(request):
    customers = Customer_Information.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def customerDetail(request, pk):
    customers = Customer_Information.objects.get(id=pk)
    serializer = CustomerSerializer(customers, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def customerCreate(request):
    serializer = CustomerSerializer(data=request.data)
    
    message = ("¡Hay un nuevo cliente interesado! Estos son sus datos:\n"
    "Nombre: " + serializer.initial_data.get("name") + "\n"
    "Servicio de interés: " + serializer.initial_data.get("service") + "\n"
    "Correo electrónico: " + serializer.initial_data.get("email") + "\n"
    "Teléfono: " + serializer.initial_data.get("phone") + "\n"
    "Nombre de la empresa: " + serializer.initial_data.get("company") + "\n"
    "Ubicación de la empresa: " + serializer.initial_data.get("company_location") + "\n"
    "Cargo: " + serializer.initial_data.get("company_position") + "\n"
    "Hora deseada para atender llamadas: " + serializer.initial_data.get("appointment_time") + "\n"
    "Consulta adicional: " + serializer.initial_data.get("additional_question"))
    #print(message)
    WhatsApp_Message = client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',
        to='whatsapp:+573153633210'
    )


    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)