print("=== โปรแกรมคำนวณ BMI ===")

weight = float(input("กรอกน้ำหนัก (กก.): "))
height = float(input("กรอกส่วนสูง (เมตร): "))

bmi = weight / (height ** 2)

print("BMI =", round(bmi,2))

if bmi < 18.5:
    print("ผอม")
elif bmi < 25:
    print("ปกติ")
elif bmi < 30:
    print("อ้วน")
else:
    print("อ้วนมาก")