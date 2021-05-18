
# Django safedelete
   * Xoá một đối tượng nhưng vẫn có thể khôi phục lại nếu muốn(khi xoá mềm)
   * Thêm một trường 'deleted=DatetimeFiedls' trong mỗi model,mặc định là Null(),khi người dùng xoá đối tượng (.delete()) thì đó là thay đổi trường deleted=thời gian xoá(với sort_delete), 
khi truy vấn bình thường sẽ bỏ qua các đối tượng này
   * pip install django-safedelete
### Các kiểu xoá : _safedelete_policy
   * SOFT_DELETE(mặc định): 
      * Xoá mềm đối tượng,chỉ áp dụng với đối tượng đó,không làm mất dữ liệu
(trường deleted= thời gian xoá),có thể khôi phục(undeleted())
      * Các đối tượng có nó làm khoá ngoại vẫn không thay đổi
   * SOFT_DELETE_CASCADE: 
      * Thực hiện xoá mềm trên đối tượng đó và cả các đối tượng có nó là khoá  ngoại,cách xoá tương tự như SOFT_DELETE,
      * Khi khôi phục cũng đồng thời khôi phục các đối tượng có nó làm khoá ngoại bị xoá theo trước đó
   * HARD_DELETE:
      * Xoá khỏi cơ sở dữ liệu, không thể khôi phục,như xoá bình thường,xoá cả những đối tượng liên quan nhận làm khoá ngoại
      * có thể chuyển sáng xoá mềm : obj.delete(force_policy=SOFT_DELETE)
   * HASD_DELETE_NOCASCADE: 
      * HASD_DELETE: nếu không là khoá ngoại của một đối tượng khác
      * SORT_DELETE : nếu là khoá ngoại của một đối tượng khác
   * NO_DELETE: không thể xoá, nếu xoá cần dùng sql thô
###  _safedelete_visibility
* DELETED_INVISIBLE(mặc định): các đối tượng xoá mềm vẫn có thể được hiển thị khi truy cập thông qua  một đối tượng có nó làm khoá ngoại(không áp dựng cho ngược lại,từ đối tượng là khoá ngoại . đến đối tượng được xoá mềm)

* DELETED_VISIBLE_BY_FIELD: như trên ,+ có thể truy cập đối tượng xoá mềm bằng get,filter


### Truy vấn 
   * SafeDeleteManager (_safedelete_visibility = DELETED_INVISIBLE): 
       * Trả về danh sách các đối tượng không bị xoá
   * SafeDeleteAllManager(_safedelete_visibility = DELETED_VISIBLE): 
       * Tất cả (chưa xoá + xoá mềm)
   * SafeDeleteDeletedManager(_safedelete_visibility = DELETED_ONLY_VISIBLE): 
       * Các đối tượng bị xoá mềm
   * Model.objecst.all() :
       * Danh sách các đối tượng chưa bị xoá(không bao gồm xoá mềm)
   * Model.all_objects.all() or (Model.objetcs.all_with_deleted()) : 
       * Danh sách các đối tượng bao gồm cả các đối tượng đã được xoá mềm
   * Model.deleted_objetcs.all() of (objects.deleted_only()): 
       * danh sách các đối tượng được xoá mềm
   * undelete(): 
       * chuyển từ xoá mềm -> bình thường(nếu là SOFT_DELETE_CASCADE thì sẽ bao gồm cả những đối tượng có nó là khoá ngoại)
   * save() :
     * keep_deleted=True : Không phục hồi mô hình nếu nó đã được xoá mềm

### Source code : https://github.com/Giang-Nguyenn/Ftech_Training/tree/main/django1/MultiTenant/Shared_DB_Schema
objects
deleted_objects
all_object
undelete()
delete_objects.
