# So sánh hiệu suất 
## 1.Hiệu suất của Serializers với ModelSerializer
### Test lấy ra list 500/1000(bản ghi) với hai cách như sau: 
  * Dữ liệu  một bản ghi trong list lấy ra: 
  
     ![Serializers_ModelSerializer-list_task](https://github.com/Giang-Nguyenn/Ftech_Training/blob/main/Reports/Images/list_task1.PNG)
     
  * TH1:serializer.Serializer(Serializer) với fileds(read_only=True).
    ![serializer.Serializer với fileds(read_only=True)](https://github.com/Giang-Nguyenn/Ftech_Training/blob/main/Reports/Images/TaskReadOnlySerializers1.PNG)
   
  * TH2:serializer.ModelSerializer(ModelSerializer).
    ![serializer.Serializer với fileds(read_only=True)](https://github.com/Giang-Nguyenn/Ftech_Training/blob/main/Reports/Images/TaskModelSerializers.PNG)
### Kết quả:
 *  **Lần 1:**
   ![ketqua-Serializers_ModelSerializer_lần 1](https://github.com/Giang-Nguyenn/Ftech_Training/blob/main/Reports/Images/serializers1.PNG) 
   * Từ biểu đồ cho thấy Serializer cho kết quả nhanh hơn so với ModelSerializer và giá trị trung bình của Serializer và ModelSerializer lần lượt là: 
     *  Seralizer=174,55(ms)
     *  ModelSerializer=195,45(ms)
 *  **Lần 2:**
   ![ketqua-Serializers_ModelSerializer_lần 2](https://github.com/Giang-Nguyenn/Ftech_Training/blob/main/Reports/Images/serializers2.PNG) 
   * Từ biểu đồ cho thấy Serializer cho kết quả nhanh hơn so với ModelSerializer giá trị trung bình của Serializer và ModelSerializer lần lượt là
     *  Seralizer=186,9(ms)
     *  ModelSerializer=192,85(ms)
  * Giải thích kết quả:
    * Vì Modelserializer tốn nhiều thời gian để đánh giá và xác nhận dữ liệu
   
## 2.Hiệu suất của query (all-select_related-perfetch_related)
### Test lấy ra list 500/1000(bản ghi) có mối quan hệ khoá ngoại với User và Projects
* Dữ liệu một bản ghi trong list lấy ra:

 ![list_task-all-select_related](https://github.com/Giang-Nguyenn/Ftech_Training/blob/main/Reports/Images/list_task2.PNG)
 
*  Queryset:
 * TH1: Task.objects.all()
 * TH2: Task.objects.select_related('project','user')  
* UserReadOnlySerializer với ProjectReadOnlySerializer có mối quan hệ với task:
  ![User+ProjectReadOnlySerializer](https://github.com/Giang-Nguyenn/Ftech_Training/blob/main/Reports/Images/User+Project_ReadOnlySerializers.PNG)
* Serializer được dùng:

  ![Serializer](https://github.com/Giang-Nguyenn/Ftech_Training/blob/main/Reports/Images/TaskReadOnlySerializers.PNG)
  
### Kết quả
 ![ketqua_all-select_related](https://github.com/Giang-Nguyenn/Ftech_Training/blob/main/Reports/Images/all-select_related.PNG)
 * Từ biểu đồ cho thấy việc query với select_related nhanh hơn so với all,và giá trị trung bình của all() và select_related lần lượt là:
   * all= 1164(ms)
   * select_related=  261,25(ms)
 * Giải thích kết quả :
   * Việc truy vấn bằng all:Với những dữ liệu có trường liên kết với một model khác, khi muốn lấy thêm thông tin từ các mối quan hệ liên kết đó  thì phải thực hiện thêm nhiều query khác nhằm lấy thêm dữ liệu đó, số truy vấn là :1+n(n là số bản ghi lấy ra) 
   * select_related:Hoạt động bằng cách JOIN các trường của các bảng liên quan. Vì thế select_related lấy các đối tượng liên quan trong cùng 1 truy vấn CSDL,số truy vấn là:1
# Kết luận
## 1.Serializers 
* serializers.Serializers.
  * Thường dùng với dữ khi chỉ đọc(list,retrieve) các trường có read_only có hiệu suất tốt hơn 
* serializer.ModelSerializers.
  * Thường dùng với khi thêm cập nhật thay đổi (post,put,patch,delete) ,chậm hơn so với Serializers với fields(read_only=True) vì tốn nhiều thời gian để đánh giá và xác nhận các trường.
## 2.Queryset
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
* **Ảnh tổng hợp kết quả**
  ![ảnh tổng hợp](https://github.com/Giang-Nguyenn/Ftech_Training/blob/main/Reports/Images/performance.png)
