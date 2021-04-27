
# Authentication
   * Dùng để xác thực , kiểm tra yêu cầu được gửi đến từ ai
   * Một quá trình xác thực gồm 3 bước
      * Sinh ra dấu hiệu: username/password,token...
      * Lưu trữ : client,server...
      * Kiểm tra dấu hiệu có hợp lệ và đối chiếu xem của ai
***
### Các cách xác thực thường dùng
   * Basic Authentication: Xác thực bằng username,password
      * Mỗi yêu cầu gửi lên sẽ gửi kèm theo username/password(được mã hoá) , server sẽ  đối chiếu với trong csdl để kiểm tra
      * Ưu,nhược điểm:
          *  Ưu điểm: đơn giản, dễ kết hợp với phương pháp khác
          *  Nhược điểm: dễ bị lộ username/password, không thể logout,không thân thiện

      * Thường được sử dụng trong các ứng dụng nội bộ, các thư mục cấm như hệ thống CMS, môi trường development, database admin...
***

   * SessionAuthentication
      * Khi người dùng đăng nhập, server sẽ tạo ra một session của người dùng và trả về cho người dùng một session id ,người dùng sẽ dùng nó trong mỗi yêu cầu gửi lên(thường được brows lưu trong cookie và được gửi  tự động)
      * Lưu trữ : Server lưu trữ thông tin session ,client lưu trữ session_id(thường browser sẽ lưu trong cookie )
      * Ưu,nhược điểm:
          * Ưu điểm: giữ kín thông tin (do thông tin lưu phía server), dung lượng gửi trong mỗi resquest nhỏ (do chỉ cần gửi session id),không cần tác động nhiều phía client,quản lý đăng nhập người dùng
          * Nhược điểm: chiếm nhiều tài nguyên server(do phải lưu thông tin của session),khó scale nếu có nhiều server,phụ thuộc domain(vì thường dùng cookie mà cookie phụ thuộc vào domain),csrf(do session thường được lưu ở cookie)

      * Thường được dùng trong các website và những ứng dụng web làm việc chủ yếu với browser, những hệ thống monolithic do cần sự tập trung trong việc lưu session data và sự hạn chế về domain...
*** 
   * TokenAuthentication 
       * Khi đăng nhập , server sẽ tạo ra một chuỗi được mã hoá gửi cho người dùng,người dùng sẽ dùng nó để gửi kèm theo trong mỗi resquest để xác thực với server,chuỗi mã hoá này không được lưu ở server
       * Ưu,nhược điểm:
          * Ưu điểm: Server không cần lưu nhiều dữ liệu, phù hợp với nhiều loại client
          * Nhược điểm: khó quản lý,dễ bị lộ(do được lưu phía client,do đó lên thường chỉ lưu username,userid chứ không lưu password),phức tạp phần client,dung lượng truyền tải lớn(dài hơn session)...
       * Thường dùng trong các Web API của hệ thống phân tán, đa nền tảng...
***
   * Trong RestFrameWork: Cài đặt phương thức xác thực mặc định trong setting hoặc chỉ định trực tiếp với authentication_classes
        * BasicAuthetication:
            * hàm authenticate lấy phương thức xác thực ở header trong request với key Authorization nếu bắt đầu bằng basic ('Basic') rồi thực hiện giải mã chuỗi để lấy username,password
            * authenticate_credentials : xác thực username,password và trả về kết quả
        * SessionAuthentication
            * authenticate: lấy đối tượng người dùng từ resquest được gửi
            * enforce_csrf: xác thực csrf
        * Token: Tươg tự như basic nhưng chuỗi mã hoá không nhất thiết mang thông tin username/password
   
 # Permission
   *  Quyền người dùng 
   *  Cài đặt trong setting hoặc chỉ định trong permission_view_class
   *  Một số phương thức có sẵn 
        * AllowAny: truy cập không hạn chế
        * IsAuthenticated: Đã đăng nhập
        * IsAdminUser: là admin(user.is_staff là True)
        * IsAuthenticatedOrReadOnly : Đã đăng nhập hoặc chỉ đọc
   * Quyền tuỳ chỉnh :
        * Kế thừa từ lớp BasePermission
        * Ghi đè hai phương thức:
            * .has_permission(self, request, view):
            * .has_object_permission(self, request, view, obj): 
                * Cấp đối tượng
                * Được gọi khi has_permission trả về True
                * obj được lấy từ get_objects trong lớp APIView
            * Trả về True or False
    * Kết hợp nhiều quyền(với or)
