a = 3
b = 4.92
c = "itGenius"

print(a)
print(b)
print(c)
print(a, b, c)

# การสร้างตัวแปรหลายตัวในบันทัดเดียวกัน

x = y = z = 10
j, k = 5, 15
print(x, y, z)
print(j, k)

status = True
msg = False

print(status, msg)

# ตัวแปรแสดงผลรวมกับข้อความ
# วิธีที่ 1 concat string
print("ราคาขายต่อชิ้น", b, "บาท")
# วิธีที่ 2 String interpolation
# %s ข้อความ(String)
# %d เลขจำนวนเต็ม (integer)
# %f ทศนิยม (float)
print("ราคาขายต่อชิ้น %f" % b, "บาท")
print("ราคาขายต่อชิ้น %.2f" % b, "บาท")

print("ราคาขายต่อชิ้น %.2f บาท มีจำนวน %d ชิ้น" % (b, a))

# วิธีที่ 3 format string
print(f"ราคาขายต่อชิ้น {b} บาท มีจำนวน {a} ชิ้น๑")

