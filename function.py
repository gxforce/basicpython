# การสร้างฟังชั่นแบบไม่มีการ return value


def hello(name):
    print(f"Hello {name}")


# เรียกใช้งานฟังก์ชั่น hello()
hello("OO OO")

print("-------------")

# การสร้างฟังก์ชันแบบมีการ Return Value


def area(width, height):
    total = width * height
    return total


# เรียกใช้งานฟังชั่น area()

print("พื้นที่ทั้งหมด : ", area(5, 50))

print("-------------")

# ฟังชั่นแบบมีค่าเริ่มต้น


def show_info(name="", salary=0.00, lang="not define"):
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Language: {lang}")


show_info()
