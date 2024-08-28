# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:23:39 2024

@author: Student
"""


a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print("Các số theo thứ tự tăng dần là:", a, b, c)
