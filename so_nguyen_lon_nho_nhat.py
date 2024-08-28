# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:17:18 2024

@author: ADMIN
"""

def main():
    a = int(input("Nhập số nguyên thứ nhất: "))
    b = int(input("Nhập số nguyên thứ hai: "))
    c = int(input("Nhập số nguyên thứ ba: "))
    if a >= b and a >= c:
        max_num = a
    elif b >= a and b >= c:
        max_num = b
    else:
        max_num = c
    if a <= b and a <= c:
        min_num = a
    elif b <= a and b <= c:
        min_num = b
    else:
        min_num = c
    print(f"Số lớn nhất là: {max_num}")
    print(f"Số nhỏ nhất là: {min_num}")

if __name__ == "__main__":
    main()
