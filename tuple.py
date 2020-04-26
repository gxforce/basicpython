#tuple เป็น List ที่ไม่สามารถเปลี่ยนแปลงค่าได้ แต่สามารถเอา List อื่นมาเก็บในตัวเองได้
number = (5, 8, 9, 6, 4, 2, 6, 1)
mixed = (10,20,[5,4,3],True,"KONG")

print(number[2])
print(mixed[1])
print(mixed[2])
print(mixed[2][1])