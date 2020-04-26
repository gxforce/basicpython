number = [5, 8, 9, 6, 4, 2, 6, 1]
name = ["KONG", "AIR", "OOM"]
mixed = [10, 25, "KONG", "AIR"]

print(number[5])

print(name[2])
print(name)

print(mixed[1],mixed[3])


print("สมาชิกทั้งหมดของ number =",len(number))

#การสร้าง List ว่าง (empty list)
data = []

#การสร้างสมาชิกเข้าไปใน list ว่าง

data.append(10)
data.append(20)
data.append(30)

print(data)

#การ update สมาชิกใน List

data[1]=12
print(data)

#ฟังชั่นวนลูป อ่านสมาชิกทั้งหมด
for n in number:
    print(n)


#ฟังชั่นวนลูป แล้วหาผลรวม
print("------------------")
count = 0
for n in number:
    count+=n
print(count)



