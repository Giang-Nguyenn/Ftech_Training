
# Python Basic
## valiable
* Có phân biệt chữ hoa chữ thường
* bắt đầu bằng chữ ,or"_"
* có thể gán giá trị trên một dòng: x,y,z="1","2","3"
* Có thể gán một giá trí bằng nhiều biến: x=y=z="aaa"
* Biến toàn cục:được tạo bên ngoài một hàm,được sử dụng ở cả trong và ngoài hàm
* global:tạo biến toàn cục bên trong một hàm
***
## Data type
* type():lấy kiểu dữ liệu

### Number:int ,float,complex
* Không giới hạn chữ số ...
* Phần thực lấy khoảng 15 chữ số thập phân-dùng decimal lấy lấy nhiều hơn
***
### phân số:Fraction(a,b)
***
### Strings
*  "",'':dùng "" nếu trong chuỗi có dấu '',và dùng '' nếu trong chuỗi có "",nếu trong chuỗi có cả "" và '' thì dùng Escape Characters(\',\")
* '''''',""""":chuỗi nhiều dòng ,or để comment
* Chuỗi là mảng byte của các kí tự unicode
* Python không có kiểu dữ liệu kí tự,một kí tự là một chuỗi có độ dài là 1
* duyệt một chuỗi s="123": for x in s
* cắt chuỗi : s[start:end]:[start-end}
  *  s[:::]:.......
  *  chỉ mục [-a] đi từ cuối chuỗi:s[-1]=3
*  a in b:chuỗi a có tồn tại trong chuỗi b->True,False
* không thay đổi được kí tự trong chuỗi bằng index(vì...)
* Format: s="  {} {} {}"
  * s.format(a,b,c):thay thế a,b,c vào trong các cặp {}
  * có thể đặt chỉ mục từ 0 :s="  {2} {1} {0}"
 * format với '%s': "a b %s"%('c')->"a b c" (%s,r,d,f)
 * format với f'chuỗi':VD s="123",f"{s}456789"->"123456789" (chưa có :{{}})
 * chuyển list thành string: s="?".join(list)->","->"?"
***
### Escape Characters:Để chèn các kí tự không hợp lệ trong một chuỗi
* r'chuỗi':sửa các Escape Characters,làm việc với biểu thức chính quy,với file
  * VD:r"\n"->"\\n"
***
### Booleans:True ,False
* True:hầu hết các giá trị có nội dung trừ 0,rỗng
* False :bool(False),bool(None),bool(0),bool(""),bool(()),bool([]),bool({})
### Ép kiểu
***
### Operators:
* ** :lũy thừa
* //:chia toán hạng,9//2 = 4 và 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0
* **
### Lists:danh sách
* Lưu trữ nhiều giá trị trong một biến 
* thislist = ["1", 2, True] ->Có thể chứ nhiều kiểu dữ liệu,chứa cả list
* thislist1 = list(("1", "2", "3")):danh sách trong khối lệnh
* thislist[a,b]:  [a:b},[start:end:step]
* có chỉ mục phủ định:áp dụng nếu muốn tìm kiếm từ cuối list
* chèn(insert),thêm(append),mở rộng(+ or extends_không nhất thiết phải là list),xóa(remove("") or pop(i),del thislist[i],clear(xóa các phần tử trong list),del),
  * del(xóa theo chỉ mục O(n-i),có thể xóa nhiều cùng lúc),pop(xóa phần tử theo chỉ mục nếu cần giá trị trả về O(n-i)),remove(xóa phần tử theo giá trị ,giá trị đầu tiên khớp O(n)),clear(xóa tất cả phần tử trong list trả về list rỗng)
* lặp danh sách: 
  * for x in thislist :lần lượt lấy giá trí trong list gán vào x
  * Lặp qua chỉ mục: for x in range(?): x chạy từ 0 đến ?-1
  * print(x) for x in thislist
* hiểu danh sách: newlist = [expression for item in iterable if condition == True]:expression có thể chưa điều kiện(điều kiện của vòng for được dùng trước,các giá trị thỏa mãn đưa vào expression rồi so sánh với điều kiện ở đây)
  * VD: s=[x if x > 2 else x*2 for x in range(1,11,1) if x > 3] ->[4->10]
* list contructor: list(iterable),iterable(string,list...) :cấu trúc một tập hợp
* list có thể thay đổi phần tử bằng index(chuỗi không được)
* List thuộc kiểu tham chiếu -> nếu gán hai list với nhau khi thay đổi một trong hai(index) sẽ làm thay đổi cả hai->dùng list contructor,copy để không làm thay đổi cả hai,a=list(b)...
* list.sort(key=funcionname,reverse=True or False):reverse(chiều sắp xếp),key(funcition truyền vào):từng phần tử trong list sẽ được đưa vào funciton(list[1],list[2]...list[len-1]) để xử lý,rồi giá trị được trả về từ funcition đó sẽ được lấy để sắp xếp ,hàm truyền vào key chỉ có một tham số(nó là từng phần tử trong list truyền vào list[?])
***
### Tuples:lưu trữ nhiều mục trong một biến duy nhất
* Được sắp xếp theo thứ tự và không thể thay đổi(bảo vệ dữ liệu dùng làm key trong dic)
* thistuple = ("1", False,3),thistuple = tuple((1, False, "3"))
* Giống list nhưng không thể thay đổi thêm sửa xóa,muốn thay đổi thì chuyển về list()->tuple()
* tốc độ truy xuaats nhanh hơn list và chiếm ít bộ nhớ hơn list
***
### Sets
* Không có thứ tự,không trùng lặp
* thisset = {"1", True, 3}
* không thể chứa một set,list trong một set...
* tạo set rỗng(s={})->dic(tạo set rỗng bằng contructor)
*  |,&...
***
### Dictionaries
* Key:value
* Sắp xếp theo thứ tự,có thể thay đổi và không trùng lặp(key)
* Dùng các key để phân biệt
* for x in namedic:danh sách tên khóa 
* for x in namedic.values():danh sách giá trị 
* for x,y in namedic.items():danh sách cả khóa và giá trị
* lồng nhau:{key:{key:value}}
* dict.get(key,default):nếu không tìm thấy key thì lấy giá trị default
* Các cách khởi tạo:
   * khởi tạo bằng contructor
   * khởi tạo bằng mapping object: một object là một mapping object nếu chúng có đủ hai phương thức keys và __getitems__
   * Khởi tạo bằng iterable: phải có cặp (key,value) 
      * VD : ((1:2),(2:3),(3:4))
   * khởi tạo bằng keyword arguments :dict(**kwargs)
   * dùng fromkey: dict.fromkeys(iterable, value): các key lần lượt là các phần tử trong iterable và giá trị là value ,mặc định nếu không truyền value thì là none(truyền list vào value :cả list được đưa vào làm value chứ không phải từng phần trong list)
### Hashable và Unhashable...
***
### Vòng lặp
* For
* While,Do While
* else trong vòng lặp:thực thi khi vòng lặp chạy xong(không được thực hiện nếu bị break)
* pass:để trống vòng lặp nhưng không bị lỗi
* range(start,stop,step):tạo ra một chuỗi các số từ start->stop bước nhảy step,truyền vào số nguyên,dạng list nhưng không phải list
## Hàm
* def myfuncition()
* Số lượng đối số không xác định :def myfuncition(*a) và a[i] là đối số nếu muốn dùng,
  * VD: myfuncition("1","2","3") ->a[0]="1"...
* Tham số default phải ở cuối,nếu truyền thiếu tham số sẽ lấu default :def funcition(name,age=1)
* Đối số từ khóa:myfuncition(key=value,,)->thứ tự đối số không quan trọng
* Đối số từ khóa tùy ý:def myfuncition(**a) và a["key"] là đối số nếu muốn dùng
  * VD:myfuncition(key1="1",key2="2",key3="3")->a["key1"]=1...
* Tham số mặc định:gọi hàm mà không truyền đối số sẽ sử dụng tham số mặc định
* danh sách dưới dạng đối số
* truyền một list,tuple... vào hàm :funcition(*list)->funcition(list[0],list[1],...,list[len(list)-1])
* pass:dùng để viết trước hàm để trống mà không lỗi
* có thể thay đổi tham số nhưng chỉ trong nội bộ hàm(dùng global để đổi ngoài hàm)
* có thể return về nhiều giá trị
* yield:
* **

### lambda:đối số :biểu thức  :có thể nhận nhiều đối số nhưng chỉ có một biểu thức
 * VD Lambda x,y,z :x+y+z  :tính tổng 3 số x,y,z
* được sử dụng khi cần một hàm trong thời gian ngắn,kết hợp với các hàm khác lớn hơn
* ngắn gọn nhưng khó kiểm soát,debug

***
## Class
* class không cần thân hàm vẫn có thể gán được thuộc tính
* hàm khởi tạo __init__(self):"chỉ có một hàm khởi tạo duy nhất(khác với các nn khác)",self đại diện cho bản thân đối tượng được tạo ra
* thuộc tính có thể gọi bằng việc tạo ra đối tượng hoặc dùng trực tiếp tên class của nó(classname.nameat)->khi thay đổi một thuộc tính trong lớp thông qua tên lớp thì thuộc tính đó cũng dduocj cập nhật với các đối tượng được tạo ra từ lớp đó
* có thể thay đổi thuộc tính thông qua hàm contructor...
* Thay đổi thuộc tính thông qua đối tượng thì chỉ đối tượng đó được áp dụng(thay đổi qua lớp thì thay đổi cả)
* classmethod:thay đổi thuộc tính class (cls,?) :cls đại diện cho lớp ->khi cập nhật sẽ thay đổi tất cả giá trị thuộc tính của cả các đối tượng(gọi qua tên lớp hay đối tượng cũng đều cập nhật cho tất cả)
  * Thường được dùng để tạo đối tượng,xử lý trước các thông tin đưa vào trước khi tạo ra một đối tượng
* staticmethod :hàm không cần truyền vào self vẫn được
* Kế thừa :class nameclass(class) :kế thừa các thuộc tính và phương thức của lớp cha(kể cả contructor)
  * có thể viết laiji các thuộc tính và phương thức của lớp cha(supper...)
  * Phương thức đặc biệt:_namemethod_
    * __init__
    * __str__
    * __repr__
    * __len__ 


## Module
* Module là các mã thư viện Python ,và có thể tái sử dụng.
* Import module:import modulemodule as ?
* liệt kê tất cả tên hàm,biến :dir(modulename)
* nhập một bộ phân trong module: from modulename import ?

## Pip 
* quản lý gói ,module 
* py -m pip install --upgrade pip;cập nhật,(-m)
* pip help
* pip install +tên gói(==: để chỉ định gói cài đặt): cài đặt gói
* pip list : liệt kê các gói
* pip freeze > requirements.txt :ghi danh sách các gói cài đặt vào file
* pip install -r requirements.txt :cài đặt ,sao chép môi trường(cài các gói,thư viện trong file chỉ định),các phiên bản cũng sẽ khớp với các phiên bản trong file
* pip install --upgrade -r requirements.txt :cập nhật các phiên bản mới nhất với các gói trong file
* trong file: "=="->">=" để cài đặt các phiên bản bằng(nếu không có mới hơn ) hhay lớn hơn các phiên bản trong file(nếu có) ,", <" để chỉ định phiên bản được cài phải nhỏ hơn 
* Có thể tạo một file khác để liệt kê các công cụ bổ xung
  * bổ xung "-r filename" để khi chạy cài đặt có thể cài đặt được luôn cả các gói trong file khác
* pip uninstall :gỡ gói(trước khi gỡ lên kiểm tra các phụ thuộc đảm bảo không ảnh hưởng tới các gói khác,show)
...

## Convention
* 4x khoảng trắng 
* chiều dài tối đa
* ngắt dòng trước các toán tử ,toán hạng(nếu dòng dài muốn ngắt)
* Dòng trống: cách 1-2 dòng với các phương thức,class ,khối code
* import lên đặt trên mỗi dòng riêng biệt
   * thư viện chuẩn->của nhà cung cấp thứ ba->cục bộ
* tên biến bắt đầu bằng hai dấu __ trong module
* dùng khoảng trắng sau các dấu ",",":",";" cho dễ nhìn
* Quy tắc đặt tên:
  * Phân biệt chữ hoa chữ thường
  * dùng _để ngăn cách 
  * tên biến,funcition chữ thường,tên hằng chữ hoa
  * tên package,module:lên viết thường ,ngắn gọn(dùng _nếu có nhiều từ),khác các module có sẵn
  * các class được viết hoa chữ cái đầu mỗi từ:ClassName
  * đặt tên với attribute/function trong class:
    * Mặc định, các attribute/function của một lớp được khai báo là public
    * protected , đặt 01 ký tự _ ở đầu tiên: _protected_attribute_name
    * private, đặt 02 ký tự _ ở đầu tiên: __private_attribute_name 
***
## Virtualenv
* Mỗi trường ảo
* Cách dùng:
  * b1:cài đặt: pip install virtualenv
  * b2:vào thư mục muốn đặt và tạo máy ảo
     *  virtualenv name(virtualenv -p /usr/bin/python? name: chỉ định phiên bản python):name là tên máy ảo, thư mục Lib có chứa thư mục site-packages, là nơi chứa các package sẽ cài đặt vào VE(virtualenv --no-site-packages name: không có package được cài đặt sẵn),thư mục Scripts chứa các file khởi chạy,và activate.bat(khởi chạy) và deactivate.bat(tắt) VE
  * cài đặt gói :pip  install và pip freeze để kiểm tra
  * Xóa một VE:rm -rf name
