from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
def test(request):
    return HttpResponse('ok 2  %s'%request.get_host().split(':')[0].lower().split('.')[0])