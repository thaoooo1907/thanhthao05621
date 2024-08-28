# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:19:22 2024

@author: ADMIN
"""

can_nang = float(input("Nhập cân nặng của bạn (kg): "))
chieu_cao = float(input("Nhập chiều cao của bạn (m): "))
bmi = can_nang / (chieu_cao ** 2)
print(f"Chỉ số BMI của bạn là: {bmi:.2f}")
if bmi < 18.5:
    print("Bạn đang thiếu cân.")
elif 18.5 <= bmi < 24.9:
    print("Bạn có cân nặng bình thường.")
elif 25 <= bmi < 29.9:
    print("Bạn bị thừa cân.")
else:
    print("Bạn bị béo phì.")
