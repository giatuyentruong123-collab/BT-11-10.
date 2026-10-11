#pseudo code cho cả người hiểu hoặc ko điều hiểu coe và thường viết bằng tiếng anh và viết in hoa1
#bai1
import random
xuc_xac=random.randint(1,6)
print(f"một số ngẫu nhiên từ 1 đến 6 là: {xuc_xac}")
#bai2
a=input("Nhập tên của bạn:")
ký_tự_ngẫu_nhiên=random.choice(a)
print(f"Ký tự ngẫu nhiên may mắn được chọn là: {ký_tự_ngẫu_nhiên}")
#bai3
tu_vung_tinh_tu=["Cool", "Fast", "Smart", "Happy"]
tu_vung_danh_tu=["Tiger", "Eagle", "Panda", "Coder"]
tinh_tu_ngau_nhien=random.choice(tu_vung_tinh_tu)
danh_tu_ngau_nhien=random.choice(tu_vung_danh_tu)
Username=tinh_tu_ngau_nhien+""+danh_tu_ngau_nhien
print(f"Username mới là:{Username}")
#bai4
Ma_Pin=""
for i in range(4):
    Ma_Pin+=str(random.randint(0,9))
print(f"Mã pin ngẫu nhiên của bạn là: {Ma_Pin}")
#bai5
N=int(input("Nhập độ dài mật khẩu:"))
chuoi_mat_khau_ngau_nhien=""
for i in range(N):
    chuoi_mat_khau_ngau_nhien+=random.choice("abcdefghijklmnopqrstuvwxyz")
print(f"Mật khẩu ngẫu nhiên của bạn là: {chuoi_mat_khau_ngau_nhien}")
#bai6
i=input("Nhập vào một câu bất kỳ:")
Cau_xao_tron=i.split()
random.shuffle(Cau_xao_tron)
print(f"Câu đã được xáo trộn ngẫu nhiên là: {' '.join(Cau_xao_tron)}")
#bai7
N1=int(input("Nhập độ dài mật khẩu: "))
for i in range(N1):
    Mat_khau+=random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*")
print(f"Mật khẩu ngẫu nhiên của bạn là: {Mat_khau}")
#bai8
N2=int(input("Viết độ dài mật khẩu: "))
for i in range(3):
    Mat_khau_ngau_nhien=""
    for j in range(N2):
        Mat_khau_ngau_nhien+=random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*")
    print(f"Phương án mật khẩu ngẫu nhiên {i+1}: {Mat_khau_ngau_nhien}")
#bai9
#Viết chương trình tạo mật khẩu độ dài N (với N ≥ 4) sao cho chắc chắn có ít nhất 1 chữ thường, 1 chữ hoa, 1 chữ số và 1 ký tự đặc biệt trong mật khẩu được sinh ra.
N3=int(input("Nhập độ dài mật khẩu (N>=4): "))
if N3<4:
    print("Độ dài mật khẩu phải lớn hơn hoặc bằng 4 ")
else:
    chuoi_mat_khau=""
    chuoi_mat_khau+=random.choice("abcdefghijklmnopqrstuvwxyz")
    chuoi_mat_khau+=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    chuoi_mat_khau+=random.choice("0123456789")
    chuoi_mat_khau+=random.choice("!@#$%^&*")
    for i in range(N3-4):
        chuoi_mat_khau+=random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*")
    chuoi_mat_khau_list=list(chuoi_mat_khau)
    random.shuffle(chuoi_mat_khau_list)
    chuoi_mat_khau="".join(chuoi_mat_khau_list)
    print(f"Mật khẩu ngẫu nhiên của bạn là: {chuoi_mat_khau}")
#bai10
Do_dai_mat_Khau=int(input("Nhập độ dài mật khẩu: "))
Co_muon_bao_gom_chu_hoa=input("Có muốn bao gồm chữ hoa (Y/N) ")
Co_muon_bao_gom_chu_thuong=input("Có muốn bao gồm chữ số (Y/N) ")
Co_muon_ki_tu_dac_biet=input("Có muốn bao gồm ký tự đặc biệt (Y/N) ")
password=""
if Co_muon_bao_gom_chu_hoa.upper()=="Y":
    password+=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
if Co_muon_bao_gom_chu_thuong.upper()=="Y":
    password+=random.choice("abcdefghijklmnopqrstuvwxyz")
if Co_muon_ki_tu_dac_biet.upper()=="Y":
    password+=random.choice("!@#$%^&*")
    while len(password)<Do_dai_mat_Khau:
        if Co_muon_bao_gom_chu_hoa.upper()=="Y":
            password+=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if Co_muon_bao_gom_chu_thuong.upper()=="Y":
            password+=random.choice("abcdefghijklmnopqrstuvwxyz")
        if Co_muon_ki_tu_dac_biet.upper()=="Y":
            password+=random.choice("!@#$%^&*")
password_list=list(password)
random.shuffle(password_list)
print(f"Mật khẩu được tạo là: {''.join(password_list)}")