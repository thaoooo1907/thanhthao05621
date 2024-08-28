# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:33:13 2024

@author: ADMIN
"""

a = float(input("Nhập số nguyên dương a: "))
b = float(input("Nhập số nguyên dương b: "))
if a <= 0 or b <= 0:
    print("Cả hai số phải là số nguyên dương.")
else:
    phan_nguyen = a // b
    phan_du = a % b
    print(f"Phần nguyên của {a} chia cho {b} là: {phan_nguyen}")
    print(f"Phần dư của {a} chia cho {b} là: {phan_du}")
