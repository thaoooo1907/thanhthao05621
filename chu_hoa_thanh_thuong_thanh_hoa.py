# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:18:27 2024

@author: Student
"""


chữ_cái = input("Nhập một chữ cái: ")
if len(chữ_cái) == 1 and chữ_cái.isalpha():
    if chữ_cái.islower():
        kết_quả = chữ_cái.upper()
    else:  
        kết_quả = chữ_cái.lower()
    print("Kết quả:", kết_quả)
else:
    print("Ký tự nhập vào không hợp lệ. Vui lòng nhập đúng một chữ cái.")
