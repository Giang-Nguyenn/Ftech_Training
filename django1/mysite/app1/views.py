# Create your views here.
from django.shortcuts import render
import datetime
from django.http import HttpResponse
from .forms import SignForm
from .forms import LoginForm
from .forms import AddPost
from .models import Post
from .models import User
from .models import Comment
from .forms import AddComment

def home(request):#trang khi chưa đăng nhập
    if request.method == "POST":
        data = LoginForm(request.POST)#lấy dữ liệu được POST
        if data.is_valid():
            isuser= User.objects.filter(username=data.cleaned_data['username'], password=data.cleaned_data['password'])
            #kiểm tra tài khoản,mật khẩu
            if isuser:#tồn tại tài khoản-> user_home
                post = Post.objects.all()
                request.session['userid'] = isuser[0].id
                request.session.set_expiry(0)
                return render(request, "app1/user_home.html", {'user': User.objects.get(pk=isuser[0].id), 'post': post})
            else : #tài khoản không tồn tại->login
                notify = "Đăng nhập không thành côngg"
                login = LoginForm
                return render(request, "app1/login.html", {'login': login,'notify':notify})
    if 'userid' in request.session: #nếu có session(đã đăng nhập trước đó) thì vào trang user_home
        userid = request.session["userid"]
        post = User.objects.get(pk=userid).post_set.all()
        return render(request, "app1/user_home.html", {'post': post,'user':User.objects.get(pk=userid)})
    # không nhận được POST nào->home
    post = Post.objects.all()
    return render(request, "app1/home.html", {'post': post})

def home_user(request):
    if 'userid' in request.session: #nếu có session(đã đăng nhập trước đó) thì vào trang user_home
        userid = request.session["userid"]
        post = User.objects.get(pk=userid).post_set.all()
        return render(request, "app1/user_home.html", {'post': post, 'user': User.objects.get(pk=userid)})
    else:#nếu không có session thì vào trang home
        post = Post.objects.all
        return render(request, "app1/home.html", {'post': post})
        # return HttpResponse("Không")

def add_post(request):#thêm một bài viết
    if 'userid' in request.session:
        if request.method == "POST":
            addpost = AddPost(request.POST)
            if addpost.is_valid():
                user = User.objects.get(pk=request.session["userid"])
                user.post_set.create(postName=addpost.cleaned_data["postName"],
                                     postContent=addpost.cleaned_data['postContent'],
                                     postCreate=datetime.datetime.now())
                userid = request.session["userid"]
                post = User.objects.get(pk=userid).post_set.all()
                return render(request, "app1/user_home.html",
                              {'post': post, 'user': User.objects.get(pk=userid)})
        addpost1 = AddPost
        return render(request, "app1/add_post.html", {'addpost': addpost1})
    else :
        login = LoginForm
        return render(request, "app1/login.html", {'login': login})

def sign(request):#form đăng kí
    sign = SignForm
    return render(request, "app1/sign.html", {'sign': sign})

def get_sign(request):# nhận yêu cầu đăng kí
    if request.method=="POST":#có yêu cầu đăng kí
        sg = SignForm(request.POST, request.FILES)
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
                return render(request, "app1/user_home.html", {'user': User.objects.get(username=sg.cleaned_data['username']),
                                                               'post': post, 'notify_success_sign': notify_success_sign})
                # notify_success="Thành công"

    else:#lỗi nào đó
        error = "Lỗi"
        sign = SignForm
        return render(request, "app1/sign.html", {'sign': sign, 'error': error})

def post_content(request,id):#hiển thị nội dung chi tiết bài viết
    if request.method == 'POST':# có comment được gửi
        if 'userid' not in request.session:# chưa đăng nhập -> login
            login = LoginForm
            return render(request, "app1/login.html", {'login': login})

        #đã đăng nhập
        cm=AddComment(request.POST)
        if cm.is_valid():
            User.objects.get(pk=request.session['userid']).comment_set.create(content=cm.cleaned_data['content'],
                                                       post=id,
                                                       create=datetime.datetime.now())
            # cm.save()
            list_comment = Comment.objects.select_related('user').filter(post=id).order_by('-id')
            post = Post.objects.get(pk=id)
            add_comment = AddComment
            return render(request, "app1/post_content.html",
                          {"post": post, 'id': id, 'list_comment': list_comment, 'add_comment': add_comment})

    # vào xem nội dung bài viết bình thường
    list_comment = Comment.objects.select_related('user').filter(post=id).order_by('-id')
    post = Post.objects.get(pk=id)
    add_comment = AddComment
    return render(request, "app1/post_content.html",
                  {"post": post, 'id': id, 'list_comment': list_comment, 'add_comment': add_comment})

def login(request):#đăng nhập
    login = LoginForm
    return render(request, "app1/login.html", {'login': login})

def logout(request):#thoát đăng nhập(xóa session và quay về trang home.html)
    request.session.flush()
    # del request.session['userid']
    post = Post.objects.all
    return render(request, "app1/home.html", {'post': post})

def A(request):
    return HttpResponse("Đây là trang A")
    # return render(request, "app1/login.html")