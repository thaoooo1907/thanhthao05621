# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:37:07 2024

@author: ADMIN
"""

ky_tu = input("Nhập một ký tự chữ thường: ")
if len(ky_tu) != 1 or not ky_tu.islower():
    print("Vui lòng nhập một ký tự chữ thường duy nhất.")
else:
    ky_tu_hoa = ky_tu.upper()
    print(f"Ký tự chữ hoa tương ứng là: {ky_tu_hoa}")
