print("Hello World")
# Exercises
#Cơ bản:

# 1.Cho hai số nguyên trả về tích nếu chúng tích nhỏ hơn 1000,nếu tích lơn hơn 1000 thì trả về tổng của chúng
# s1=lambda a,b:a*b if (a*b<1000) else (a+b)
# print("Kết quả là : ",s1(12,10))

# 2.Cho một dãy 10 số đầu tiên, Làm lại từ số đầu đến số cuối và in ra tổng của số hiện tại và số trước đó
# s2=lambda a:a+a-1 if(a!=0) else a
# for i in range(10):
#     print("Số hiện tại là {}".format(i),end="")
#     print(" Tổng của số đó và số liền trước đó là : ",s2(i))

# 3.Cho một chuỗi, chỉ hiển thị những ký tự có chỉ số chẵn.
# s3="0123456789"
# for i in range(0,len(s3),2):
#     print(s3[i],end=" ")

# print("#4.Cho một chuỗi và một số nguyên n, xóa các ký tự khỏi một chuỗi bắt đầu từ 0 đến n và trả về một chuỗi mới")
# def removeChars(str,n) :
#     return str[n:]
# print(removeChars("123456789",3))

# print("5.Cho một danh sách các số, trả về True nếu số đầu tiên và số cuối cùng của danh sách giống nhau")
# list5=[1,2,3,4,5,6,7,8,9,1]
# print("Chuỗi vừa nhập là ",list)
# def is_First_Last_Same(list):
#     if(list[0]==list[len(list)-1]):
#         return True
#     return False
# print("kết quả là : ",is_First_Last_Same(list))

# print("6.Cho một danh sách các số, hãy lặp lại và chỉ in ra những số chia hết cho 5")
# list6=[1,2,3,4,5,6,7,8,9,10,11,12]
# print("List :",list6)
# def find_Device_Five(list):
#     for i in list:
#         if(i%5==0) :
#             print(i,end=" ")
# find_Device_Five(list6)

# print("7.Trả về tổng số chuỗi con “?” xuất hiện trong chuỗi đã cho")
# str1="1234567891111"
# def Count_Chars(str,s) :
#     return str.count(s)
# print("Số lần xuất hiện là :",Count_Chars(str1,"1"))


# print("""8.In mẫu :
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5""")
# print("Kết quả :")
# for i in range(1,6,1):
#     for j in range(i):
#         print(i,end=" ")
#     print("")

# print("9.Đảo ngược một số đã cho và trả về true nếu nó giống với số ban đầu")
# # s9=1221
# # s9list=list(str(s9))
# # s9list.reverse()
# # if(list(str(s9))==s9list):
# #     print("True")
# # else:
# #     print("False")

# print("10.Cho một danh sách hai số, tạo một danh sách mới sao cho danh sách mới chỉ chứa các số lẻ từ danh sách thứ nhất và các số chẵn từ danh sách thứ hai")
# list1=[1,2,3,4,5,6,7,8,9]
# list2=[1,2,3,4,5,6,7,8,9]
# list=[]
# for i in list1:
#     if(i%2==1):
#         list.append(i)
# for i in list2:
#     if(i%2==0):
#         list.append(i)
# list.sort()
# print("danh sachs  mới là :",list)

# print("11.Viết đoạn mã tách từng chữ số từ một số nguyên, theo thứ tự ngược lại")
# a=lambda x : list(str(x))
# print(a(12345)[::-1])

# print(""" 12.Tính thuế thu nhập đối với thu nhập cho trước bằng cách tuân thủ các quy tắc dưới đây
# Ví dụ: giả sử rằng thu nhập chịu thuế là $ 45000 thì thuế thu nhập phải trả là
#
# $ 10000 * 0% + $ 10000 * 10% + $ 25000 * 20% = $ 6000.
# """)
# def Income_Tax(income):
#     if(income<10000):
#         return 0
#     elif(income<20000):
#         return (income-10000)*(10/100)
#     else:
#         return 1000+(income-20000)*(20/100)
# print("Thuế là : ",Income_Tax(45000))

# print("13.In bảng cửu chương từ 1 đến 10")
# for i in range(1,11,1):
#     print("bẳng cửu chương của {}".format(i),end=" : ")
#     for j in range(1,11,1):
#         print(i*j,end=" ")
#     print("")

# print("""14.In Mô hình một nửa kim tự tháp hướng xuống với ngôi sao (dấu hoa thị)
# * * * * *
# * * * *
# * * *
# * *
# *
# """)
# number=5
# print("Số tầng là :{}".format(number))
# for i in range(number,0,-1):
#     for i in range(i):
#         print("* ",end=" ")
#     print(" ")

# print("15.Viết một hàm có tên exponent(base, exp)trả về giá trị int của cơ số nâng lên thành lũy thừa của exp.")
# def exponent(base, exp):
#     return base**exp
# print("Kết quả là : ",exponent(5,4))




# bài tập đầu vào đầu ra

# print("1.Chấp nhận hai số từ người dùng và tính phép nhân")
# # num1=int(input("Nhập số thứ nhất :"))
# # num2=int(input("Nhập số thứ hai :"))
# # print("Kết quả là :" ,num1*num)

# print("2. Hiển thị “My Name Is James” là “My ** Name ** Is ** James” bằng cách sử dụng định dạng đầu ra của một print()hàm")
# print("My{}name{}is{}A".format('**','**','**'))

# print("3.Chuyển đổi số thập phân sang bát phân bằng cách sử dụng print()định dạng đầu ra")
# print(format(10,"o"))
# print('%o' % (10))

# print("4.Hiển thị số thực có 2 chữ số thập phân bằng cách sử dụng print()")
# print(format(12.3456789,".2f"))

# print("5.Chấp nhận danh sách 5 số thực làm đầu vào từ người dùng")
# list=[]
# for i in range(5):
#     item=float(input("nhập vào số thứ {} :".format(i+1)))
#     list.append(item)
# print("danh sách vừa nhập là : ",list)




# if else ,for loop and range
# print("1.Nhận số từ người dùng và tính tổng tất cả các số từ 1 đến số đã cho")
# sum=0;
# def Add(number):
#     global sum
#     for i in range(number+1):
#          sum=sum+i
#     return sum
# print(Add(100))

# print("2.Hiển thị thông báo “Xong” sau khi thực hiện thành công vòng lặp for")
# for i in range(10):
#     print(i,end=" ")
# else:
#     print("xong")


# print("3.Chương trình Python để hiển thị tất cả các số nguyên tố trong một phạm vi")
# def Find_Prime(start,end):
#     for i in range(start,end+1,1):
#         for j in range(2,i//2+1,1):
#             if(i%j==0):
#                 break
#         else:
#             print(i,end=" ")
# print("các số nguyên số là : ")
# Find_Prime(1,19)

# print("4.Hiển thị chuỗi Fibonacci lên đến n số hạng")
# def Fibonacci(number):
#     numt=0
#     nums=1
#     for i in range(1,number+1,1):
#         if(i==1):
#             print("0",end=" ")
#         elif(i==2):
#             print("1",end=" ")
#         else:
#             print(numt+nums,end=" ")
#             num=numt
#             numt=nums
#             nums=num+nums
# Fibonacci(10)

# print("5.Viết vòng lặp tìm giai thừa của một số bất kỳ")
# def Factorial(number):
#     kq=1
#     for i in range(1,number+1,1):
#         kq=kq*i
#     return kq
# print(Factorial(5))

# print("6.Hiển thị một số lập phương đến một số nguyên cho trước")
# a=lambda x:x**3
# print(a(4))

# print("7.Tìm tổng của dãy số 2 +22 + 222 + 2222 + .. n số hạng")
# def sum(number):
#     s=2
#     kq=0
#     if(number>1):
#         for i in range(1,number+1,1):
#             kq=kq+s
#             s=s*10+2
#         return kq
#     else:return 0
# print(sum(3))

# print("""8.In mẫu sau
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# * * * *
# """)
# def display(number):
#     for i in range(1,number+1,1):
#         for j in range(i):
#             print("*",end=" ")
#         print(" ")
#     for i in range(number-1,1,-1):
#         for j in range(i):
#             print("*",end=" ")
#         print(" ")
#     for i in range(number-1):
#         print("*",end=" ")
# display(10)

#Funcition
# print("1.Tạo một hàm có thể chấp nhận hai đối số tên và tuổi và in ra giá trị của nó")
# def funcion1(name,age):
#     print("Tên là : {}".format(name),"Tuổi là : {}".format(age))
# funcion1("A",1)

# print("2. Viết một hàm func1()sao cho nó có thể chấp nhận độ dài đối số thay đổi và in ra tất cả giá trị đối số")
# def funciton2(*s):
#     for i in s:
#         print(i)
# funciton2("1",12,123)

# print("3.Viết một hàm calculation()sao cho nó có thể nhận hai biến và tính cộng, trừ của nó. Và nó cũng phải trả về cả phép cộng và phép trừ trong một lệnh gọi trả về")
# def funcion3(a,b):
#     return a+b,a-b
# print(funcion3(1,2))

# print("4.Tạo một hàm showEmployee()theo cách mà nó phải chấp nhận tên nhân viên, nó là tiền lương và hiển thị cả hai, và nếu lương bị thiếu trong hàm hãy gọi nó sẽ hiển thị là 9000")
# def funcion4(name,salary=9000):
#     print(name,"Lương là {}".format(salary))
# funcion4("A",1000)
# funcion4("A")

# print("5. Viết hàm đệ quy tính tổng các số từ 0 đến n")
# def Sum(number):
#     if(number==1):return 1
#     if(number>1):
#         return number+Sum(number-1)
# print(Sum(100))

# print("6.Cho một chuỗi có độ dài lẻ ,trả về một chuỗi được tạo bởi ba ký tự ở giữa của một chuỗi đã cho")
# str="12345"
# middle=len(str)//2
# print(str[middle-1:middle+2])












