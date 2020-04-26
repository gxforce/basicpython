scores = {
    'john':1200,
    'bobby':2000,
    'janny':3000
}

print(scores)
print(scores['bobby'])

#เพิ่มสมาชิกใหม่เข้า dictionry
scores['roger']=3200

print(scores)

print("-----------------------------")

#การสร้าง dictionary ว่าง
points={}


#เพิ่มค่าเข้า dictionary ว่าง
points['mr_a']=10.2
points['mr_b']=20.2
points['mr_c']=30.2

print(points)

print("-----------------------------")

for k,v in scores.items():
    print(k,v)
