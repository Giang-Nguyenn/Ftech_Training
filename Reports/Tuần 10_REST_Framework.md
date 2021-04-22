# So sánh hiệu suất
## Serializers 
* serializers.Serializers
  * Thường dùng với dữ khi chỉ đọc(list,retrieve) các trường có read_only có hiệu suất tốt hơn 
* serializer.ModelSerializers
  * Thường dùng với khi thêm cập nhật thay đổi (post,put,patch,delete) ,chậm hơn so với Serializers với fields(read_only=True) vì tốn nhiều thời gian để đánh giá và xác nhận các trường.
* Kết quả so sánh: Images/performance.png
## Queryset
* .All()
  * Với những dữ liệu có trường liên kết với một model khác, khi muốn lấy thêm thông tin từ các mối quan hệ liên kết đó  thì phải thực hiện thêm nhiều query khác nhằm lấy thêm dữ liệu đó -> chậm hơn 
  * Số truy vấn = 1+n(số bản ghi ) 
 * .select_related():
   * Hoạt động bằng cách JOIN các trường của các bảng liên quan. Vì thế select_related lấy các đối tượng liên quan trong cùng 1 truy vấn CSDL -> nhanh hơn
   * Dùng cho mối quan hệ: 1-1,1-n
   * Số truy vấn =1
 * .perfetch_related():
   * Thực hiện một truy vấn khác sau đó kết hợp và  thực hiện  giảm các cột dư thừa
   * Thường dùng cho các mối quan hệ :m2m,n-1 (dùng được cho cả 1-1,1-n)
   *  Số truy vấn = 2
 -> hiệu năng tăng dần : .all() - perfetch_related - select_related
 * Kết quả so sánh: Images/performance.png
