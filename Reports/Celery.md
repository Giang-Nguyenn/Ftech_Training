# Celery
### Message Queue:
* Là hàng đợi chứa nhiều message
* Là một hộp thư, cho phép các thành phần/service trong một hệ thống (hoặc nhiều hệ thống), gửi thông tin cho nhau.
* Việc lấy message theo cơ chế FIFO(First In First Out): vào trước ra trước
* Message Queue thường có những thành phần:
    * Message: Thông tin được gửi đi (text, binary hoặc JSON)
    * Message Queue: Nơi chứa những message trên, cho phép producer và consumer có thể trao đổi với nhau
    * Producer: Chương trình/service tạo ra thông tin, đưa thông tin vào message queue
    * Consumer: Chương trình/service nhận message từ message queue và xử lý
    * Một chương trình/service có thể vừa là producer, vừa là consumer
* Ưu điểm:
    * Đảm bảo duration/recovery:Do message đã được lưu trong queue, khi 1 service đang xử lý nhưng bị crash hoặc lỗi, ta không lo bị mất dữ liệu; vì có thể lấy message từ trong queue ra và chạy lại. 
Trong 1 hệ thống có nhiều consumer, nếu 1 consume bị crash cũng không làm sụp toàn hệ thống
    * Phân tách hệ thống: Giúp phân tách hệ thống thành nhiều service nhỏ hơn, mỗi service chỉ xử lý 1 chức năng nhất định
    * Hộ trợ rate limit, batching
    * Dễ scaling hệ thống : có thể điều chỉnh số lượng consume thích hợp với các thời điểm khác nhau
* Nhược điểm:
    * Khó xử lý đồng bộ
    * Làm phức tạp thêm hệ thống
    * Cần đảm bảo message format
    * Cần Monitoring Queue
* Một số message queue: RabbitMQ,Kafka

### Celerry
* Là một hệ thống quản lý hàng đợi xử lý task thời gian thực
* Input của celery cần kết nối với một loại message broker còn output có thể kết nối tới một hệ thống backend để lưu trữ kết quả
* Cơ chế: 
   * Celery thường dùng một message broker để điều phối task giữa các clients và worker. 
Để tạo một task mới client sẽ thêm một message vào queue, broker sau đó sẽ chuyển message này tới worker
   * Các loại Broker được hỗ trợ:RabbitMQ,Redis,SQS
* Các chức năng chính của Celery:
   * Monitor: giám sát các job/task được đưa vào queue
   * Scheduling: chạy các task lập lịch (giống cronjob)
   * Workflows: tạo một luồng xử lý task
   * Time & Rate Limits: kiểm soát số lượng task được thực thi trong một khoảng thời gian, thời gian một task được chạy,...
   * Resource Leak Protection: kiểm soát tài nguyên trong quá trình xử lý task
   * User Component: cho phép người dùng tự customize các worker.


