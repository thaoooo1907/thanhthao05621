# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:15:56 2024

@author: Student
"""

def kiem_tra_thoi_gian(giờ, phút, giây):
    
    if 0 <= giờ <= 23 and 0 <= phút <= 59 and 0 <= giây <= 59:
        return True
    return False

try:
    giờ = int(input("Nhập giờ (0-23): "))
    phút = int(input("Nhập phút (0-59): "))
    giây = int(input("Nhập giây (0-59): "))

    if kiem_tra_thoi_gian(giờ, phút, giây):
        print("Giờ, phút, giây nhập vào là hợp lệ.")
    else:
        print("Giờ, phút, giây nhập vào không hợp lệ.")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
