from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from .utils import tenant_from_request
from .models import Projects
from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectsSerializers
# Create your views here.

class ProjectsView(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializers

    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)
    
    def create(self, request, *args, **kwargs):
        ten=tenant_from_request(request).id
        request.data.update({'tenant': ten})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(request.data, status=status.HTTP_201_CREATED, headers=headers)





def test(request):
    return HttpResponse('ok %s'%request.get_host().split(':')[0].lower().split('.')[0])
