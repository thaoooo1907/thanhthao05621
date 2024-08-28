# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:21:32 2024

@author: ADMIN
"""

so_xe = input("Nhập số xe (gồm 4 chữ số): ")
if len(so_xe) != 4 or not so_xe.isdigit():
    print("Số xe phải gồm 4 chữ số.")
else:
    nut = set(so_xe)
    so_nut = len(nut)
    print(f"Số xe của bạn có {so_nut} nút.")
