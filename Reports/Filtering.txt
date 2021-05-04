# Feltering
* Dùng để lọc lấy một tập con 
* Lọc trong get_queryset:
   * Thêm bộ lọc cho queryset: Modelname.objects.filter(filed='?'),các dữ liệu dùng để lọc lấy trên url
   * Lọc theo url : self.kwargs['id'] với url : /user/<int:id>
       * .filter(id=self.kwargs['id'])
   * Lọc theo tham số truy vấn : self.request.query_params.get('id') với /user?id=?
       * .filter(id=self.request.query_params.get('id'))
   * Lọc chung : cho phép tạo các bộ lọc phức tạp hơn
      * cài đặt phần phụ trợ của bộ lọc trong setting(DEFAULT_FILTER_BACKENDS) hoặc chỉ định trực tiếp trên lớp 
          * filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
## DjangoFilterBackend
   * Cài đặt: install->INSTALLED_APPS->add vào setting(hoặc thêm trực tiếp trong class)
   * Lọc đơn giản : filterset_fields = ['id', 'name'...]: tự động tạo một FilterSet lớp cho các trường nhất định, 
   với lookup_expr='exact'
## SeachFilter
   * Các SearchFilter chỉ được áp dụng nếu có một search_fields bộ thuộc tính. Các search_fields là list các fileds với thuộc tính như CharField,TextField.
   * tra cứu liên quan trên ForeignKey hoặc ManyToManyField sử dụng __
   * Đối với các trường JSONField và HStoreField,có thể lọc dựa trên các giá trị lồng nhau trong cấu trúc dữ liệu bằng cách sử dụng cùng một ký hiệu gạch dưới kép
   *  Mặc định,các tìm kiếm sẽ sử dụng đối sánh từng phần không phân biệt chữ hoa chữ thường
   * Hành vi tìm kiếm có thể bị hạn chế bằng cách thêm các ký tự khác nhau vào search_fields.
       * '^' Bắt đầu với tìm kiếm.
       * '=' Kết hợp chính xác.
       * '@' Tìm kiếm toàn văn. (Hiện tại chỉ hỗ trợ phần phụ trợ PostgreSQL của Django .)
       *Tìm kiếm '$' Regex.
## OrderingFilter
   * Sắp xếp
   * Chỉ định trường được sắp xếp : ordering_fields = ['?', '?',...]
   * Nếu không chỉ định ordering_fields, mặc định cho phép lọc trên bất kỳ trường nào có thể đọc được trên bộ tuần tự được chỉ định bởi serializer_class.

## FilterSet
   * Kế thừa từ django_filters.FilterSet
   * giống với ModelForm , có thể ghi đè  và thêm mới các bộ lọc
   * một số thuộc tính :
       * filed_name: tên của trường để lọc ,có thể duyệt qua quan hệ bằng cách thêm "__" với các mô hình có liên quan
       * lookup_expr: để sử dụng khi lọc : gt(lớn hơn),lt(nhỏ hơn),contains(so sánh char)...
       * exclude: mặc định là False
       * required
    * Một số bộ lọc :
       * CharFilter: so sánh với kí tự đơn giản
       * BooleanFilter: khớp với boolean
       * ChoiceFilter : khớp với các giá trị được truyền vào trong choices 
       * DateFilter,TimeFilter,DateTimeFilter tương ứng với DateField,TimeField,DateTimeField
       * IsoDateTimeField để hỗ trợ lọc ngày tháng được định dạng ISO 8601
       * NumberFilter
       VD: price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
       url: ?price_gt=1-> lọc price lớn hơn 1
       * nếu không chỉ định mặc định lookup_expr='exact'
   * có thể tạo bộ lọc bằng Meta.fields,tương tự như form hay serializer
       * model: tên Model mẫu 
       * fileds: list các trường được chỉ định trong bộ lọc
       * Mặc định là tra cứu chính xác(exact)
       * custom fields với class Meta :
           VD: fields = {
            'price': ['lt', 'gt'],
        }
        -> Tạo ra bộ lọc  với :price_lt,price_gt
       * cũng có thể sử dụng với các mối quan hệ bằng cách sử dụng "__"
### Tích hợp với DRF
   * thêm bộ lọc bằng filter_class
       * filter_class=?
   *việc sử dụng filterset_fields và filterset_class kết hợp không được hỗ trợ.
