# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:37:48 2024

@author: Student
"""


hinh = input("Nhập hình (v: hình vuông, n: hình chữ nhật, t: hình tròn): ").strip().lower()


if hinh == 'v':
   
    canh = float(input("Nhập chiều dài cạnh của hình vuông: "))
    chu_vi = 4 * canh
    dien_tich = canh * canh
    print(f"Kết quả:\nChu vi = {chu_vi}\nDiện tích = {dien_tich}")

elif hinh == 'n':
   
    chieu_rong = float(input("Nhập chiều rộng của hình chữ nhật: "))
    chieu_dai = float(input("Nhập chiều dài của hình chữ nhật: "))
    chu_vi = 2 * (chieu_rong + chieu_dai)
    dien_tich = chieu_rong * chieu_dai
    print(f"Kết quả:\nChu vi = {chu_vi}\nDiện tích = {dien_tich}")

elif hinh == 't':
   
    import math
    ban_kinh = float(input("Nhập bán kính của hình tròn: "))
    chu_vi = 2 * math.pi * ban_kinh
    dien_tich = math.pi * ban_kinh ** 2
    print(f"Kết quả:\nChu vi = {chu_vi:.2f}\nDiện tích = {dien_tich:.2f}")

else:
    print("Loại hình không hợp lệ. Vui lòng nhập 'v' cho hình vuông, 'n' cho hình chữ nhật, hoặc 't' cho hình tròn.")
