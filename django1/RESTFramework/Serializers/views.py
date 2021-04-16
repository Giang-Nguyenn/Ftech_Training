from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.http import Http404
from django.shortcuts import redirect
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination

from .models import Student
from .serializers import StudentSerializers,SchoolSerializers,StudentSerializers1
from rest_framework.viewsets import ModelViewSet

# Create your views here.


# class StudentCRUD(APIView):

#     def get(self, request):
#         list_student = Student.objects.all() # trả về dạng objetc
#         datas = StudentSerializers(list_student, many=True) # Dạng objects +model
#         return Response(data=datas.data, status=status.HTTP_200_OK) # Dạng json

#     def post(self, request): # post/resquest
#         data = StudentSerializers(data=request.data) # data post+Serializers 
#         if data.is_valid():
#             # return HttpResponse('%s'%data.data) # Json
#             Student.objects.create(name=data.data['name'],
#                                    phone=data.data['phone'],
#                                    address=data.data['address'],
#                                    email=data.data['email'],
#                                    birth_day=data.data['birth_day']
#                                    )
#             return Response('Ok', status=status.HTTP_200_OK)
#         return Response('No', status=status.HTTP_400_BAD_REQUEST)

# class StudentList(APIView):
#     def get(self,request):
#         list_student=Student.objects.all()
#         datas=StudentSerializers(list_student,many=True)
#         return Response(data=datas.data,status=status.HTTP_200_OK)
        
#     def post(self,request):
#         data=StudentSerializers(data=request.data)
#         if data.is_valid(raise_exception=True):
#             Student.objects.create(name=data.data['name'],
#                                    phone=data.data['phone'],
#                                    address=data.data['address'],
#                                    email=data.data['email'],
#                                    birth_day=data.data['birth_day']
#                                    )
#             return Response('Thành công',status=status.HTTP_200_OK)
#         return Response('Error',status=status.HTTP_400_BAD_REQUEST)

# class StudentDetail(APIView):
#     def get_object(self,id):
#         try :
#             return Student.objects.get(pk=id)
#         except Student.DoesNotExist:
#             raise Http404

#     def get(self,request,id):
#         student=self.get_object(id)
#         datas=StudentSerializers(student)
#         return Response(data=datas.data,status=status.HTTP_200_OK)


#     def delete(self,request,id):
#         student=self.get_object(id)
#         student.delete()
#         return Response('Xoá thành công', status=status.HTTP_200_OK)

#     def put(self,request,id):
#         student=self.get_object(id)
#         student_put=StudentSerializers(student,data=request.data)
#         if student_put.is_valid(raise_exception=True):
#             student_put.save()
#             return Response(data=student_put.data,status=status.HTTP_200_OK)
#         return Response('Error',status=status.HTTP_400_BAD_REQUEST)

# class StudentList(generics.ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
#     # pagination_class = None
#     pagination_class = LimitOffsetPagination

class StudentList1(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    pagination_class=PageNumberPagination


class StudentList(APIView):
    def get(self,request):
        list_student=Student.objects.all()
        datas=StudentSerializers(list_student,many=True)
        return Response(data=datas.data,status=status.HTTP_200_OK)
        
    def post(self,request):
        data=StudentSerializers1(data=request.data)
        if data.is_valid(raise_exception=True):
            Student.objects.create(name=data.data['name'],
                                   phone=data.data['phone'],
                                   address=data.data['address'],
                                   email=data.data['email'],
                                   birth_day=data.data['birth_day']
                                   )
            return Response('Thành công',status=status.HTTP_200_OK)
        return Response('Error',status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    def get_object(self,id):
        try :
            return Student.objects.get(pk=id)
        except Student.DoesNotExist:
            raise Http404

    def get(self,request,id):
        student=self.get_object(id)
        datas=StudentSerializers(student,many=True)
        return Response(data=datas.data,status=status.HTTP_200_OK)



def home(request):
    return HttpResponse('demo')
