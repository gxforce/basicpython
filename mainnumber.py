# Import ทั้งหมดทุกฟังชั่นใน Module
#import numbers


# เรียกใช้งาน
# print(numbers.factorial(5))
# print("----")
# print(numbers.fibonacci(5))

# ---------------------------------------------------

# Import มาบางฟังชั่น ใน Module
#from numbers import factorial

# print(factorial(5))

# ---------------------------------------------------

# Import มาบางฟังชั่น ใน Module
#from numbers import factorial,fibonacci

# print(factorial(5))
# print("----")
# print(fibonacci(5))

# ---------------------------------------------------

# Import มาบางฟังชั่น ใน Module
#from numbers import*

# print(factorial(5))
# print("----")
# print(fibonacci(5))
# ---------------------------------------------------

# Import Module มาแล้วเปลี่ยนชื่อ Alias
from numbers import factorial as fa, fibonacci as fi
print(fa(5))
print("----")
print(fi(5))
