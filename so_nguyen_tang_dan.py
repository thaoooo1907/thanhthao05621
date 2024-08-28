# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:27:09 2024

@author: Student
"""


N = input("Nhập một số nguyên N: ")

if N.isdigit():
    
    chữ_số = list(N)
    chữ_số.sort()
    số_mới = ''.join(chữ_số)
    print("Số có các chữ số theo thứ tự tăng dần là:", số_mới)
else:
    print("Vui lòng nhập một số nguyên dương.")
