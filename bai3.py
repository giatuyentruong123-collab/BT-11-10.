#sep la phan cach
# bai1 
a=input("Nhập họ tên của bạn ")
b=int(input("Nhập tuổi của bạn "))
c=2026-b
print(f"xin chào {a}, năm nay bạn {c} tuổi")
#bai2
A = input("Nhập từ thứ nhất: ")
B = input("Nhập từ thứ hai: ")
C = input("Nhập từ thứ ba: ")
print(A, B, C, sep="-")
print("chúc bạn học tốt", end="!!!")
#bai3
ho_ten = input("Nhập họ và tên: ")
ho_ten = ho_ten.strip().title()
print(ho_ten)
#bai4
van=input("nhập vào đây một câu văn ")
print(len(van))
print(van.upper())
#bai5
chuoi = input("Nhập từ hoặc dãy số: ")
chuoi1=input("Nhập từ hoặc dãy số: ")
print(chuoi==chuoi1)
print(chuoi[::-1])
#bai6
ma_dinh_danh=input("Nhập mã định danh để lấy ra các thông tin: ")
index=ma_dinh_danh.find(" ")
print("Loại:",ma_dinh_danh[:index])
print("năm sản xuất:",ma_dinh_danh[index+1:index+5])
print("Tên sản phâm:",ma_dinh_danh[index+5:])
#cách 2
#print("loại",ma_dinh_danh[0:2])
#print("năm sản xuất:",ma_dinh_danh[3:7])
#print("Tên sản phẩm:",ma_dinh_danh[8:12])
#bai7
Name=input("Nhập họ tên của nhân viên ")
Name=Name.strip().lower()
print(Name.replace(" ",".")+"@gmail.com")
print(f"email của công ty {Name} là: {Name.replace(' ','@gmail.com')}")
#bai8
tieu_de=input("Nhập tiêu đề thông báo ")
print("="*40)
print("*"+tieu_de.center(38)+"*")
print("="*40)
#bai9
Chuoi_khoang_trang=input("Nhập vào một chuỗi bị lẫn khoảng trắng thừa ở 2 đầu ")
Chuoi_da_lam_sach=Chuoi_khoang_trang.strip().lower()
print("Độ dài thực tế sau khi làm sạch:",len(Chuoi_da_lam_sach))
print("3 ký tự đầu tiên của chuỗi:",Chuoi_da_lam_sach[:3])
print("3 ký tự cuối cùng của chuỗi:",Chuoi_da_lam_sach[-3:])
#bai10
Name_hung=input("Nhập tên thật của bạn ")
Mau=input("Nhập màu yêu thích của bạn ")
con_vat=input("nhập con vật yêu thích của bạn ")
Name_hung = Name_hung.strip().title()
Mau = Mau.strip().title()
con_vat = con_vat.strip().title()
biệt_danh = Mau +" "+ con_vat + " " + Name_hung
print("="*40)
print("*"+"Thẻ Siêu Anh Hùng".center(38)+"*")
print("Nhập tên thật cua bạn:",Name_hung)
print("Biệt danh của bạn là:",biệt_danh)
print("="*40)
