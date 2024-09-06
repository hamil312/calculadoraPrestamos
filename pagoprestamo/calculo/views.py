import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from math import pow
# Create your views here.
class calculoView(APIView):
    def get(self, request, *args, **kwargs):
        id_cliente=request.GET.get('id')
        nombre_cliente=request.GET.get('nombre')
        monto=request.GET.get('monto')
        plazo=request.GET.get('plazo')
        tasa_interesa=request.GET.get('interes')
        interes_mensual=pow(1+(float(tasa_interesa)/100), (1/12)) -1
        valor_interes = float(monto)*pow((1+interes_mensual), float(plazo))-float(monto)
        valor_total = valor_interes+float(monto)
        return Response("El prestamo realizado por "+nombre_cliente+" identificado por el número "+ id_cliente+" por un monto de "+monto+" a un plazo de "+plazo+" meses "+" con una tasa de interes del "+tasa_interesa+"% tendrá un valor de "+str(valor_total), status=status.HTTP_200_OK)