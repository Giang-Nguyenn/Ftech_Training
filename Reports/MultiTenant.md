# Multi Tenant
### SaaS 
* Software-as-a-Service:mô hình phân phối dịch vụ ứng dụng phần mềm; nhà cung cấp không bán sản phẩm phần mềm mà bán dịch vụ dựa trên phần mềm đó. Nhà cung cấp tạo ra và duy trì một phần mềm chạy trên nền web, và khách hàng có thể truy cập từ xa thông qua internet sau khi trả một khoản phí đăng ký định kỳ (hàng tháng, quý, năm).
### Multi Tennan
* Đa nhiệm phần mềm
* Một cơ sở hạ tầng(server,database...) nhưng cho phép nhiều người có thể sử dụng,
* Một hệ thống web application có nhiều khách hàng cùng sử dụng nhưng dữ liệu giữa các khách hàng hoàn tập độc lập, khách hàng này không thể truy cập vào dữ liệu của khách hàng khác.
VD: Một hệ thống chấm công có nhiều công ty cùng dùng,mặc dù chung server,web,db...nhưng mỗi công ty chỉ có thể truy cập vào dữ liệu công ty mình ,độc lập với công ty khác

* Ưu điểm :
   * Chi phí thấp hơn do chỉ sử dụng cơ sở hạ tầng phía nhà cung cấp.
   * Người sử dụng không cần bận tâm về việc cập nhật các tính năng và cập nhật mới, họ cũng không cần phải trả phí bảo trì hoặc chi phí khổng lồ vì đó là việc của nhà cung cấp.
   * Kiến trúc Multi tenant phục vụ hiệu quả tất cả mọi người từ các khách hàng nhỏ, có quy mô có thể không đảm bảo cơ sở hạ tầng chuyên dụng. Chi phí phát triển và bảo trì phần mềm được chia sẻ, giảm chi tiêu, dẫn đến tiết kiệm được chuyển cho bạn, khách hàng.
   * Hỗ trợ dịch vụ tốt hơn.
   * Mang lại lợi ích lâu dài cho các nhà cung cấp cũng như người dùng, có thể là về mặt bảo trì, chi phí đầu tư hoặc phát triển.

* Khuyết điểm
   * Khó backup database riêng lẻ từng tenant
   * Dữ liệu phìm to nhanh chóng Khó khăn khi scale hệ thống.

## Các phương án Multi Tenant
* PA1:Cùng chung một cơ sở dữ liệu (database), chia sẻ bảng (table)
    * Tất cả các bảng liên quan đều có 1 khóa ngoại.Đó là cơ sở để phân biệt giữa các người dùng
    * Ưu điểm 
        * Thiết kế lưu trữ đơn giản.
        * Dễ cho việc phát triển.
        * Không gặp phải vấn đề đồng bộ cấu trúc bảng trong quá trình phát triền.
    * Nhược điểm 
        * Không độc lập database nên việc một người dùng có thể xem dữ liệu của người dùng khác nếu có quyền truy cập SQL, phân quyền trên SQL phức tạp.
        * Vấn đề backup, restore dữ liệu cho từng khách hàng phức tạp(cần phải viết truy vấn riêng), chỉ có thể backup cho tất cả.
        * Vấn đề phát sinh phức tạp khi dữ liệu phình to, rất khó khăn trong việc backup, restore...
        * Khó khăn khi scale hệ thống.
    * Ứng dụng
        * Phương án này chỉ dùng làm những hệ thống nhỏ, ít dữ liệu, phát sinh dữ liệu không lớn.

PA2: Cùng chung database, chia sẻ schema
   * Database -> schema -> table -> column
   * Schema: là một namespace dùng để gom nhóm các table có chung một đặc điểm nào đó đễ dễ dàng quản lý.
      * trong schema tên table là duy nhất
      * trong 1 database ta có thể đặt tên 2 table giống nhau, với điều kiện chúng phải thuộc 2 schema khác nhau.
      * Ưu điểm của schema
         * Giúp nhóm các Database Object lại với nhau cho dễ quản lý
         * Cho phép phân quyền ở schema tăng tính bảo mật
   * Hướng thiết kế này sử dụng một cơ sở dữ liệu, mỗi tenant tương ứng 1 schema(có tenant mới sẽ tạo thêm một  schema từ schema chuẩn vào database). Có một schema chung để quản lý những các dữ liệu chung, quản lý thông tin về tenants. Cấu trúc các bảng ở tất cả các tenant đều giống nhau. 
   * Cần 1 schema chuẩn để dựa vào đó tạo ra tenant mới trong quá trình thêm mới tenant.
   * Ưu điểm: Khi bạn phân nhóm các table lại thì sẽ rất dễ dàng quản lý, và bạn có thể phân quyền quản lý từng schema cho từng user khác nhau, đây chính là điểm mạnh của schema.
   * Nhược Điêm:
        * Chung 1 database, dữ liệu sẽ nhanh chóng phìng ra to sẽ phát sinh rất nhiều vấn đề
        * Vấn đề backup, restore dữ liệu cho từng tenant phức tạp, có thể backup cho tất cả bằng tool. Còn muốn backup, restore cho từng tenant thì phải viết câu lệnh riêng, phức tạp.
        * Khó khăn khi scale hệ thống.
        * Số lượng schema trong 1 database là có giới hạn( 2^31-1=2,147,483,647=số lượng tối đa kiểu dữ liệu số nguyên ?) .
        * Đồng bộ những thay đổi cấu trúc table trong schema là vấn đề cần được quan tâm.

* PA3:Mỗi tenant một database.
    * Hệ thống sẽ gồm 1 database chung (chuyên để quản lý các phần như danh sách tenant, user, role ...), 1 database tenant chuẩn (chứa dữ liệu chuẩn), và các tenant khác.
    * Mỗi tenant sẽ là 1 database, người dùng sẽ có quyền truy cập vào database chung và database tenant của user đó.


## Django with MultiTenant 
#### Chung database chia sẻ schema
* Dữ liệu được lưu chung trên database,scheme và phân biệt dữ liệu giữa các tenant bằng một khoá ngoại đặc trưng cho người đó
* Xác định tenant : thường xác định bằng sub host
* Mỗi tenant có một tên miền riêng đặc trưng,duy nhất
* vd : localhost
* -> host1.localhost
* -> host2.localhost



* host1,host2 sẽ đặc trưng cho mỗi tenant(model) ,và là khoá ngoại cho tất cả các bảng để có thể phân biệt dữ liệu của các người dùng khác nhau.
* có một method để xác định người dùng từ các sub host
* Mỗi khi thêm dữ liệu vào các bảng thì khoá ngoại tenant sẽ được thêm vào để có thể phân biệt được dữ liệu của những người khác nhau
* Khi truy vấn dữ liệu sẽ thêm một bước lọc  : .filter(tenant=tenant) để lấy ra giữ liệu của tenant đó

# Source Code : PA1: https://github.com/Giang-Nguyenn/Ftech_Training/tree/main/django1/MultiTenant/Shared_DB_Schema
