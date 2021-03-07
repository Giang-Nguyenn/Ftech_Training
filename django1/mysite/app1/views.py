from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import SignForm
from .models import Post

def Home(request):
    post = Post.objects.all
    return render(request, "app1/home.html", {'post':post})

def Sign(request):
    sign = SignForm
    return render(request, "app1/sign.html", {'sign': sign})

def getSign(request):
    if request.method=="POST":
        sg = SignForm(request.POST)
        if sg.is_valid :
            sg.save()
            return HttpResponse("Thành công")
    else:
        return HttpResponse("Lỗi")

def postContent(request,id):
    post = Post.objects.get(pk=id)
    return render(request, "app1/post_content.html", {"post": post})


def Login(request):
    # return HttpResponse("Đây là trang Login")
    return render(request, "app1/login.html")
def A(request):
    return HttpResponse("Đây là trang A")
    # return render(request, "app1/login.html")