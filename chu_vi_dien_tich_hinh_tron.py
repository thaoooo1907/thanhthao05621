# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:13:16 2024

@author: ADMIN
"""

import math
ban_kinh = float(input("Nhập bán kính của hình tròn: "))
chu_vi = 2 * math.pi * ban_kinh
dien_tich = math.pi * ban_kinh**2
print(f"Chu vi của hình tròn là: {chu_vi:.2f}")
print(f"Diện tích của hình tròn là: {dien_tich:.2f}")
