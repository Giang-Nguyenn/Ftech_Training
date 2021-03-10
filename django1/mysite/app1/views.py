# Create your views here.
from django.shortcuts import render
import datetime
from django.http import HttpResponse
from .forms import SignForm
from .forms import LoginForm
from .forms import AddPost
from .models import Post
from .models import User

def Home(request):#trang khi chưa đăng nhập
    if request.method == "POST":
        data = LoginForm(request.POST)#lấy dữ liệu được POST
        if data.is_valid():
            isuser= User.objects.filter(username=data.cleaned_data['username'],password=data.cleaned_data['password'])
            #kiểm tra tài khoản,mật khẩu
            if isuser:#tồn tại tài khoản-> user_home
                post = Post.objects.all()
                request.session['userid'] = isuser[0].id
                request.session.set_expiry(0);
                return render(request, "app1/user_home.html", {'username': data.cleaned_data['username'],'post':post})
            else : #tài khoản không tồn tại->login
                notify = "Đăng nhập không thành côngg"
                login = LoginForm
                return render(request, "app1/login.html", {'login': login,'notify':notify})
    if 'userid' in request.session: #nếu có session(đã đăng nhập trước đó) thì vào trang user_home
        userid= request.session["userid"]
        post= User.objects.get(pk=userid).post_set.all()
        return render(request, "app1/user_home.html", {'post': post,'username':User.objects.get(pk=userid).username})
    # không nhận được POST nào->home
    post = Post.objects.all()
    return render(request, "app1/home.html", {'post': post})
def HomeUser(request):
    if 'userid' in request.session: #nếu có session(đã đăng nhập trước đó) thì vào trang user_home
        userid= request.session["userid"]
        post= User.objects.get(pk=userid).post_set.all()
        return render(request, "app1/user_home.html", {'post': post,'username':User.objects.get(pk=userid).username})
    else:#nếu không có session thì vào trang home
        post = Post.objects.all
        return render(request, "app1/home.html", {'post': post})
        # return HttpResponse("Không")
def addPost(request):#thêm một bài viết
    if request.method == "POST":
        addpost = AddPost(request.POST)
        if addpost.is_valid():
            user=User.objects.get(pk=request.session["userid"])
            user.post_set.create(postName= addpost.cleaned_data["postName"],postContent=addpost.cleaned_data['postContent'],postCreate=datetime.datetime.now())
            userid = request.session["userid"]
            post = User.objects.get(pk=userid).post_set.all()
            return render(request, "app1/user_home.html",{'post': post,'username':User.objects.get(pk=userid).username})
    addpost1= AddPost
    return render(request, "app1/add_post.html", {'addpost': addpost1})
def Sign(request):#form đăng kí
    sign = SignForm
    return render(request, "app1/sign.html", {'sign': sign})

def getSign(request):# nhận yêu cầu đăng kí
    if request.method=="POST":#có yêu cầu đăng kí
        sg = SignForm(request.POST)
        if sg.is_valid() :
            issg=User.objects.filter(username=sg.cleaned_data['username'])#kiểm tra xem tên đăng nhập đã tồn tại chưa
            if issg:#tên đăng nhập đã tồn tại
                sign_notify_error= "Tồn tại tên đăng nhập này"
                sign = SignForm
                return render(request,"app1/sign.html", {'sign': sign,'sign_notify_error':sign_notify_error})
            else:# hợp lệ->lưu vào cơ sở dữ liệu-> vào trang user_home
                sg.save()
                notify_success_sign="Thành công"
                post = Post.objects.all()
                request.session['userid'] = User.objects.get(username=sg.cleaned_data['username']).id
                request.session.set_expiry(0);
                return render(request, "app1/user_home.html", {'username': sg.cleaned_data['username'], 'post': post,'notify_success_sign':notify_success_sign})
                # notify_success="Thành công"

    else:#lỗi nào đó
        error = "Lỗi"
        sign = SignForm
        return render(request, "app1/sign.html", {'sign': sign, 'error': error})

def postContent(request,id):#hiển thị nội dung chi tiết bài viết
    post = Post.objects.get(pk=id)
    return render(request, "app1/post_content.html", {"post": post})


def Login(request):#đăng nhập
    login = LoginForm
    return render(request, "app1/login.html", {'login': login})

def Logout(request):#thoát đăng nhập(xóa session và quay về trang home.html)
    request.session.flush()
    # del request.session['userid']
    post = Post.objects.all
    return render(request, "app1/home.html", {'post': post})
    # return render(request, "app1/home.html", {'login': login})

def A(request):
    return HttpResponse("Đây là trang A")
    # return render(request, "app1/login.html")