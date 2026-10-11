#bai1
a=str(input("Nhập họ tên của bạn:"))
b=int(input("Nhập tuổi của bạn:"))
c=float(input("Nhập chiều cao của bạn:"))
d=bool(input("Bạn có phải hoc sinh không?"))
print(a)
print(b)
print(c)
print(d)
#bai2
A=15
B=3.14
C="Python"
D=True
print(type(A))
print(type(B))
print(type(C))
print(type(D))
#bai3
E=1
e=2
E+e
print(E+e)
E-e
print(E-e)
E*e
print(E*e)
E/e
print(E/e)
#bai4
A1=10
B1=3
print("Chu vi và diện tích hình chữ nhật là")
print("Chu vi:", 2 * (A1 + B1))
print("Diện tích:", A1 * B1)
#bai5
Toan=8
Van=7.5
Anh=9
print("Điểm trung bình 3 môn là:",(Toan+Van+Anh)/3)
#bai6
n=int(input("đổi phút thành giờ và phút:"))
print(n//60,"giờ ",end="")
print(n%60,"Phút")
#bai7
A2=int(input("Nhập số nguyên 3 chữ số bất kì:"))
print("Số hàng trăm là:",A2//100)
print("Số hàng chục là:",(A2//10)%10)
print("Số hàng đơn vị là:",A2%10)
#bai8
A3=2
N=5
print("Kết quả của phép toán:",A3^N)
print("Kết quả của lũy thừa:",A3**N)
#bai9
I=float(input("Nhập độ C:"))
print("Độ F là:",I*9/5+32)
#bai10
M=str(input("Nhập tên sản phẩm:"))
N1=float(input("Nhập giá sản phẩm:"))
O=int(input("Nhập số lượng sản phẩm:"))
print("Tổng số tiền phải trả là:",N1*O)
#bai11
F=str(input("Nhập một số nguyên:"))
F=bool(F)
print(F)
#bai12
Age=int(input("Nhập tuổi của một người:"))
print(6 <= Age <= 18)
# bai 13
X = int(input("Nhập một số: "))
print(10 <= X <= 50)
# bai 14
V = int(input("Nhập tuổi xem đủ điều kiện không: "))
print(V > 10)
has_ticket = bool
print(has_ticket)
#bai15
n = int(input("Nhập một số nguyên: "))
print(n % 2 == 0)
#bai16
A4=float(input("Nhập Một số "))
B4=float(input("Nhập một số "))
print(A4+B4)
print(A4-B4)
print(A4 * B4)
print(A4 / B4)
print(A4 // B4)
print(A4 % B4)
print(A4 ** B4)
#bai17
ten = input("Nhập tên sản phẩm: ")
don_gia = float(input("Nhập đơn giá: "))
so_luong = int(input("Nhập số lượng: "))
giam = float(input("Nhập phần trăm giảm giá: "))
thanh_tien = don_gia * so_luong
tien_giam = thanh_tien * giam / 100
phai_tra = thanh_tien - tien_giam
print("Sản phẩm:", ten)
print("Đơn giá:", don_gia)
print("Số lượng:", so_luong)
print("Giảm giá:", giam, "%")
print("Thành tiền:", thanh_tien)
print("Tiền giảm:", tien_giam)
print("Tiền phải trả:", phai_tra)
#bai18
toan = float(input("Nhập điểm Toán: "))
van = float(input("Nhập điểm Văn: "))
anh = float(input("Nhập điểm Anh: "))
diem_trung_binh = (toan + van + anh) / 3
ket_qua = diem_trung_binh >= 8 and toan >= 6.5 and van >= 6.5 and anh >= 6.5
print(ket_qua)
#bai19
nam_sinh = int(input("Nhập năm sinh: "))
nam_hien_tai = int(input("Nhập năm hiện tại: "))
tuoi = nam_hien_tai - nam_sinh
print(tuoi >= 13)
print(13 <= tuoi <= 18)
print(tuoi < 18)
#bai20
ho_ten = input("Nhập họ tên: ")
tuoi = int(input("Nhập tuổi: "))
toan = float(input("Nhập điểm Toán: "))
van = float(input("Nhập điểm Văn: "))
anh = float(input("Nhập điểm Anh: "))
dtb = (toan + van + anh) / 3
dtb_8 = dtb >= 8
ba_mon = toan >= 6.5 and van >= 6.5 and anh >= 6.5
do_tuoi = 13 <= tuoi <= 18
du_dieu_kien = dtb >= 8 and toan >= 6.5 and van >= 6.5 and anh >= 6.5 and 13 <= tuoi <= 18
print("Họ tên:", ho_ten)
print("Tuổi:", tuoi)
print("Điểm Toán:", toan)
print("Điểm Văn:", van)
print("Điểm Anh:", anh)
print("Điểm trung bình:", f"{dtb:.2f}")
print("Điểm trung bình >= 8:", dtb_8)
print("Cả 3 môn >= 6.5:", ba_mon)
print("Tuổi từ 13 đến 18:", do_tuoi)
print("ĐỦ ĐIỀU KIỆN HỌC BỔNG:", du_dieu_kien)
