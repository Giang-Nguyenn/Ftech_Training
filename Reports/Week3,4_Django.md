
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
  * Mỗi class model nếu không chỉ định trường khóa chính thì tự động sẽ được thêm một trường id(tự động tăng-id = models.AutoField(primary_key=True)),nếu được chỉ định khóa chính sẽ không thêm vào nữa,mỗi class model cần có một trường khóa chính
  * verbose_name : một tên khác của trường,trong các mối quan hệ (1-1,1-n,n-n) phải chỉ định rõ verbose_name="?"(vì đối số đầu tiên liên quan đến mô hình khác tham chiếu đến),không viết hoa chữ cái đầu tiên.
  * Có các kiểu dữ liệu như :
    * Kiểu cột: database sẽ liệu những kiểu này: integer,char,text...
         * CharField:cho các chuỗi có kích thước nhỏ,phải có maxleng->truy xuất nhanh hơn TextField
         * FileField(to_upload,max_length,**option) 
      * ForeignKey( to,on_delete,**option):mối quan hệ nhiều-một :to(bảng tham chiếu đến),on_delete()...
        * to:bảng tham chiếu đến,tham chiếu đệ quy đến bản thân ('self'),tham chiếu đến một mô hình chưa xác định('modelname')  
           * mô hình ở ứng dụng khác: 'appname.modelname'
        * on_delete:
          * CASCARE: khi xóa một đối tượng thì đối tượng liên quan chứa ForeignKey đến nó cũng bị xóa theo
          * Protect: ngăn việc xóa đối tượng đượng tham chiếu đến
          * Restrict: 
      *  ManyToManyField(to, **options):quan hệ nhiều nhiều
      *  OneToOneField(to,on_delete,parent_link=?,**option): 1-1,là khóa chính của một mô hình khác,có thể truy cập đến các trường của nhau
      * (https://docs.djangoproject.com/en/1.11/ref/models/fields/#model-field-types)
  * Kiểu widget: khi sử dụng form (class,id :để liên kết với css)
  *  các tùy chọn :
     * null: True or False :nếu True thì lưu các giá trị rỗng là null trong database
     * blank: được phép trống hay không
     * khi CharFieldcó cả hai (unique=True, blank=True) thì null=True được yêu cầu để tránh vi phạm ràng buộc duy nhất khi lưu nhiều đối tượng với giá trị trống.
     * choices
     * default: mặc định
     * help_text: đoạn text ngắn mô tả trường này
     * primary_key:chỉ định khóa chính,nếu không chỉ định sẽ tự động tạo một trường "id",mỗi model chỉ có một trường làm khóa chính(tương ứng với null=False và unique=True)
     * unique: nếu bằng True thì nó là duy nhất trong toàn bộ bảng
       * unique_for_date,month,year: không có hai bản ghi có giá trị cùng date,month,year
     * Field.editable():Nếu False trường sẽ không được hiển thị trong quản trị viên hoặc bất kỳ trường nào khác ModelForm. Chúng cũng được bỏ qua trong quá trình xác nhận mô hình . Mặc định là True.
     * ...
     https://docs.djangoproject.com/en/3.1/ref/models/fields/
* class :Meta: lưu trữ các thông tin cấu hình về model đó: sắp xếp dữ liệu(ordering),tên bảng(db_table) ...
  *  https://docs.djangoproject.com/en/3.1/ref/models/options/
  *  thừa kế


*  truy vấn dữ liệu:
  * Thêm dữ liệu :  
      * modelname(:,...) : tạo dữ liệu cho modelname nhưng chưa lưu -> save()->create
      * với (n-n) tạo thể hiện -> add
  * Truy xuất các dữ liệu :
    * modelname.objects.all(): lấy toàn bộ dữ liệu của bảng modelname
      * modelname.objects.get(option): lấy dữ liệu có lọc
    * modelname.modelname1_set.all() : lấy dữ liệu ở bảng modelname1 với modelname là khóa ngoại
      * modelname.modelname1_set.all() : lấy toàn bộ
        * [start:end:step]: dữ liệu lấy từ {start:end:step],không hỗ trợ chỉ mục âm
      * modelname.modelname1_set.create(:,:) : tạo
    * filter: Khớp với các điều kiện 
    * excute: không khớp với các điều kiện :
    * order-by : 
      * sắp xếp (+:như Meta cài đặt,- :giảm dần,?:ngẫu nhiên)
      * order-by('filed1','filed2'...): thứ tự filed1->filed2...
      * order-by(): không theo thứ tự
      * order-by('?').order-by('?').order-by('?') : chỉ gọi order-by cuối
      * sắp xếp theo trường trong mô hình khác 'modelname__name'
    * resever() :đảo ngược thứ tự,gọi tiếp sẽ khôi phục như bản đầu
      * resever()[:?] : thứ tự trả về : n,n-1,...
    * distinct(): loại bỏ trùng lặp :
    * value('filed1','filed2'...) : trả về các trường tương ứng filed1,filed2...(value(): trả về hết các trường)...
    *  values_list() : chỉ trả về giá trị chứ không trả về một dic
    * có thể gọi filter(), order_by() , values() xen kẽ và không theo thứ tự
    * union():kết hợp hai kết quả với nhau
    * intersection()
    * difference()
    * select_related()
    * prefetch_related() 
  * cập nhật (save()),tạo và cập nhật(name.objects.create),
  * xóa dữ liệu :delete(): trả về số đối tượng bị xóa và dic cho số lần xóa của các đối tượng,xóa cả các đối tượng có khóa ngoại chỉ vào đối tượng vừa xóa
  * lọc dữ liệu: get(), filter() và exclude()
    * lọc số lượng bản ghi [:],không hỗ trợ chỉ số âm
    * Biểu thức tìm kiếm : <tên thuộc tính>__<kiểu tìm kiếm>=<giá trị> Vd: .filter(pub_date__lte='dd-mm-dd')
    *  Tìm kiếm đa bảng: <tên khóa ngoại>__<tên thuộc tính của bảng khác>=<giá trị>
  * Tạo form: kế thừa từ lớp forms.Form
    *  Field ở đây là để tạo form HTML còn field bên model là để tạo bảng CSDL(tham số nhận vào sẽ được lấy để hiển thị ra form),các input lable sẽ được tự sinh

 * Migrations
  * makemigrations:  chịu trách nhiệm tạo di chuyển mới dựa trên những thay đổi models,lưu lịch sử thay đổi model
    * --name :đặt tên 
  * migrate:  áp dụng vào cơ sở dữ liệu, không áp dụng di chuyển.
  * sqlmigrate:  hiển thị các câu lệnh SQL để di chuyển.
  * showmigrations:  liệt kê các lần di chuyển và trạng thái của chúng.
  * Đảo ngược : py manage.py migrate appname ?...
    * đảo ngược tất cả zero

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

  * autoescape(on,off) :chuyển đổi các kí tự đặc biệt trong HTML sang một dạng mã-> bảo vệ website,tắt trên từng biến (| safe)
  * có thể gọi được phương thức nhưng là các phương thức không tham số 
  * filter
    * for,if..
    * {% firstof var1 var2 var3 %}:xuất ra biến đầu tiên khác false
    * include
    * load :tải về tập mẫu tùy chỉnh
    * now :hiển thị thời gian hiện tại
      *  Thời gian {% now "jS F Y H:i" %}
    * regroup : nhóm các danh sách theo một thuộc tính chung
    * url: {% url 'urlname' v1 v2 ...%}
    * add :đầu tiên sẽ ép kiểu về số nguyên, nếu không được sẽ trả về rỗng
      * {{ value|add:"2" }} : -> value=value+2...
      * [1, 2, 3] |add [4, 5, 6]-> [1, 2, 3, 4, 5, 6]
    * {{ value|addslashes }}:thêm dấu \ trước dấu nháy,hữu ích cho việc thoát chuỗi trong csv
    *  capfirst :viết hoa chữ cái đầu tiên,nếu đầu tiên không phải là chữ cái sẽ không có tác dụng
    * {{ value|cut:"?" }} : loại bỏ tất cả "?" trong chuỗi value
      * {{ "1 2 3" |cut:" "}} ->"123"
    * date : định dạng ngày
    * {{ value|default_if_none:"?" }} : nếu và chỉ nếu giá trị value là none thì sử dụng giá trị mặc định
    * {{ value|dictsort:"name" }}: lấy danh sách từ điển và sắp xếp theo khóa được cung cấp
    * dictsortreversed :ngược lại với dictsort
    * {{ value|divisibleby:"?" }} : trả về True nếu value chia hết cho ?
       * {{ value=10 | divisibleby:"2" }} -> True
    * escape :thoát chuỗi 
    * escapejs :thoát các kí tự trong js
    * {{ value|first }} : trả về phần tử đầu tiên trong danh sách
      * ['a', 'b', 'c']->'a'
    * {{ value|floatformat:? }} :làm tròn ? chữ số phần thập phân,mặc định là 1 chữ số(nếu không có đối số mặc định là -1)
    * join
      * ['a', 'b', 'c'] |join:" // " -> "a // b // c"
    * {{ value|last }} : trả về phần tử cuối trong list
    * {{ value|length }} : trả về độ dài 
    * {{ value|linebreaks }} : ngắt dòng 
      * 123\4 -> <p>123<br>4</p>
    * {{ value|linebreaksbr }} : chuyển "\"-><br>
    * {{ value|linenumbers }} :hiển thị văn bản với số dòng,đánh số dòng cho các dòng
    * {{ value|lower/upper }} : chuyển chuỗi thành chữ thường,chữ hoa
    * {{ value|make_list } : chuyển thành danh sách,với số nguyên sẽ chuyển thành chuỗi rồi thành danh sách
    * {{ value|random }} :trả về một phần tử ngẫu nhiên trong danh sách 
    * {{ value|slice:"start:end" }} :trả về một phần của danh sách
    * {{ value|slugify }}: chuyển đổi khoảng trắng thành dấu gạch nối,loại bỏ các ký tự không phải là chữ và số, dấu gạch dưới hoặc dấu gạch nối,chuyển đổi thành chữ thường.
    * {{ value|wordcount }} : trả về số lượng từ
    * static: để liên kết các tập tin tĩnh trong STATIC_ROOT
  * Model Form :Kế thừa từ lớp form
     * class Meta:
        * model  : liên hệ với các lớp trong model
        * fields : chỉ định các trường hiển thị trong form 
  * trong form luôn có {% csrf_token %} để bảo mật.

