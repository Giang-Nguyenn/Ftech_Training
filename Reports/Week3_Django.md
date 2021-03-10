
# Django
## Mô hình MVT(Model-View_Template)
  * Model: chứa các mô hình cho cơ sở dữ liệu(Các class tương ứng với các bảng,được kế thừa từ lớp model)
  * View :tương tác với dữ liệu và gọi template
  * Template :Hiển thị
->Tương tự MVC:(Model-Model),(View-Template),(Controler-View)


***


## django-admin startproject projectname:Tạo project với tên name
 * manage.py:tương tác với dự án Django(py manage.py để xem list)
 * Thư mục bên trong mysite/là gói Python thực cho dự án của bạn. Tên của nó là tên gói Python mà bạn sẽ cần sử dụng để nhập bất kỳ thứ gì bên trong nó (ví dụ mysite.urls).
 * __init__.py: tệp trống , để cho biết nó là một gói
 * settings.py: Cài đặt và cấu hình :
   **INSTALLED_APPS:Chứa tên của tất cả các ứng dụng Django được kích hoạt trong phiên bản Django này
    'polls.apps.PollsConfig',
    'django.contrib.admin',#trang web quanr trị
    'django.contrib.auth',#hệ thống xác thực
    'django.contrib.contenttypes',#khuôn mẫu cho các nội dung
    'django.contrib.sessions',#phiên làm việc
    'django.contrib.messages',#khung tin nhắn
    'django.contrib.staticfiles',#khuôn mẫu để quản lý các tệp tĩnh
   **MIDDLEWARE
   **ROOT_URLCONF:mặc định sẽ tải đường dẫn này đầu tiên khi vào trang web
   **TEMPLATES
   **DATABASES:database 
   **AUTH_PASSWORD_VALIDATORS
   **STATIC_URL:url tĩnh
 * urls.py: Có các url,điều hướng các url
 * asgi.py: 
 * wsgi.py: 

* py manage.py startapp appname:Tạo một web app tên là appname
  * migrations: chứa các lịch sử của model ,mỗi khi migrations thì sẽ có một file dc tạo
  để lưu các thay đổi trong model
  * migarate : đồng bộ hóa các thay đổi model với cơ sở dữ liệu 
    ** init
    ** 0001 initial :chứa câu lệnh tạo các bảng khi chạy migrate
  * admin: liên quan đến trang admin,xem những bảng,dữ liệu nào sẽ hiển thị trên trang admin
    * admin.site.register(modelname) 
  * apps: cấu hình ứng dụng
  * models :chứa các models(như bảng trong database) có trong app
  * test: 
  * urls:cấu hình các urls,điều hướng khi có các url khác nhau
  * views : điều khiển ,tương tác với dữ liệu và gọi đến các template(hiển thị)
  * templates->appname:chứa các template để hiển thị(HTML),khi gọi chỉ cần : appname/namefile.html
  * static-> appname: chứa các file tĩnh như css,scrips,...
    + lấy file trong template: {% load staticfiles %}-> link(static 'appname/?' ): static=/appname/static/


***


### Model 
  * Thừa kế từ lớp models
  * Có các kiểu dữ liệu như :
    * Kiểu cột: database sẽ liệu những kiểu này: integer,char,text...
         * CharField:cho các chuỗi có kích thước nhỏ,phải có maxleng->truy xuất nhanh hơn TextField
         * ForeignKey( to,on_delete,**option):mối quan hệ nhiều-một :to(bảng tham chiếu đến),on_delete()...
        *  ManyToManyField(to, **options):quan hệ nhiều nhiều
        *  OneToOneField(to,on_delete,parent_;link=?,**option): 1-1
        * (https://docs.djangoproject.com/en/1.11/ref/models/fields/#model-field-types)
  * Kiểu widget: khi sử dụng form (class,id :để liên kết với css)
  *  các tùy chọn :
     *  null: True or False :nếu True thì lưu các giá trị rỗng là null trong database
     * blank: được phép trống hay không
     * choices
     * default: mặc định
     * help_text: đoạn text ngắn mô tả trường này
     * primary_key:chỉ định khóa chính,nếu không chỉ định sẽ tự động tạo một trường "id",mỗi model chỉ có một trường làm khóa chính
     * unique: nếu bằng True thì nó là duy nhất trong toàn bộ bảng
     * ...
* class :Meta: lưu trữ các thông tin cấu hình về model đó: sắp xếp dữ liệu(ordering),tên bảng(db_table) ...
  *  https://docs.djangoproject.com/en/3.1/ref/models/options/
  *  thừa kế
* một số câu truy vấn dữ liệu: 
  * modelname(:,...) : tạo dữ liệu cho modelname nhưng chưa lưu -> save()
  * modelname.objects.all(): lấy toàn bộ dữ liệu của bảng modelname
     * modelname.objects.get(option): lấy dữ liệu có lọc
  * modelname.modelname1_set.all() : lấy dữ liệu ở bảng modelname1 với modelname là khóa ngoại
    * modelname.modelname1_set.all() : lấy toàn bộ
    * modelname.modelname1_set.create(:,:) : tạo
* cập nhật (save()),tạo và cập nhật(name.objects.create),
* lọc dữ liệu: get(), filter() và exclude()
  * lọc số lượng bản ghi [:],không hỗ trợ chỉ số âm
  * Biểu thức tìm kiếm : <tên thuộc tính>__<kiểu tìm kiếm>=<giá trị> Vd: .filter(pub_date__lte='dd-mm-dd')
  *  Tìm kiếm đa bảng: <tên khóa ngoại>__<tên thuộc tính của bảng khác>=<giá trị>
* Tạo form: kế thừa từ lớp forms.Form
  *  Field ở đây là để tạo form HTML còn field bên model là để tạo bảng CSDL(tham số nhận vào sẽ được lấy để hiển thị ra form),
các input lable sẽ được tự sinh



 ###  View
 * chạy vào đường dẫn được cài đặt trong ROOT_URLCF->urlpatterns[] ->appname.urls...
 * path(route,view,kwargs,name)
   * route:chứa các mẫu url,định dạng bằng Regex hoặc chuỗi
    * '<name>/'': VD:'/123/' :giá trị 123 được lưu trong biến name có thể được dùng trong các hàm views sau đó  
   * view: nếu tìm được mẫu phù hợp sẽ gọi đến view
   * kwargs : từ khóa dưới dạng cặp (key:value), vẫn có thể dùng ở các url dưới  
   * name:đặt tên cho các url,thuận tiện khi gọi url trong template:(url 'urlname: name' +)
 * re_path()
 * Regex:
   * 
 * views.py
 +chứa các hàm,class tương tác với database và gọi đến template
 +funcition view ,class view(có thể kế thừa)
 get_objects_or_404(Class,pk,...=?)(Không có sẽ trả về lỗi)
+namespace: để tránh nhầm lẫn giữa các url: các app khác nhau có các name giống nhau(app_name="namespace")
+để chỉ định những thuộc tính được hiển thị trong trang admin:
  +  tài khoản admin:
    + py manage.py createsuperuser
  + cấu hình trong admins:để tùy chọn những dữ liệu được hiển thị trong trang quản trị
     + tạo một class(classA) kế thừa từ lớp admin.ModelAdmin và khai báo một list có tên các thuộc tính muốn hiện trong trang admin : 
       * fields = ['?', '?','?']
       * admin.site.register(model,classA)
  * render( request , template_name , context = None , content_type = None , status = None , using = None )
    * request : đối tượng yêu cầu
    * template_name : trang html
    * context : các cặp (key : value) để hiển thị trong te,plate_name
    * contect_type : mặc định là text/html
    * status : mã trạng thái cho phản hồi mặc định là 200
    * using


  * @require_http_methods( request_method_list ): chỉ chấp nhật các phương thức yêu cầu cụ thể

  * Lấy dữ liệu từ form: cần dùng cleaned_data để lấy dữ liệu được post lên
    * Cần data.is_valid()

  * Session:
  >>> color = request.session['color'] 
>>> color1 = request.session.get('color', 'red')
   * lấy giá trị :
      * request.session['name']
      * request.session.get('name','default')
   * Thiết lập
      * request.session['name'] = 'value'
   *  Xóa session:
      * del request.session['name']: xóa một session
      * request.session.flush() : xóa toàn bộ dữ liệu session
   * Thiết lập thời gian tồn tại :
      * request.session.set_expiry(?) : nếu 0 là tồn tại đến khi tắt trình duyệt
   * Kiểm tra tồn tại:
      * 'name' in request.session

***

### Ngôn ngữ template
  *  {{ variable }} :Biến
      * {{value|default:"?"}}:biến không có dữ liệu thì lấy default
      * {{name|filtename}}: bộ lọc,có thể dùng nhiều bộ lọc cùng một lúc ||
         *  Vd: {{ name|lower }}: ch
  * {% tag %} :Thẻ tag
    * Bình luận,comment: {# ???? #}h, 
    * Thừa kế :kết hợp các trang html,liên kết chúng qua các block : {% block blockname %}{% endblock %}
,các đoạn code sẽ được thay thế vào trong các khối,cần khai báo extends :{% extends "name.html" %}(luôn được đặt trước các thẻ còn lại)
  * Model Form :Kế thừa từ lớp form
     * class Meta:
        * model  : liên hệ với các lớp trong model
        * fields : chỉ định các trường hiển thị trong form 
  * trong form luôn có {% csrf_token %} để bảo mật.

