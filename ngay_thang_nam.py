# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:55:03 2024

@author: ADMIN
"""

ngay = int(input("Nhập ngày (ngày): "))
thang = int(input("Nhập tháng (tháng): "))
nam = int(input("Nhập năm (năm): "))
print(f"a) Ngày/tháng/năm: {ngay}/{thang}/{nam}")
nam_2chu_so = nam % 100
print(f"b) Ngày/tháng/năm với năm 2 chữ số: {ngay}/{thang}/{nam_2chu_so:02d}")

print(f"c) Năm/tháng/ngày: {nam}/{thang}/{ngay}")