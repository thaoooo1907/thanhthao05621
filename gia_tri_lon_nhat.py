# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:27:45 2024

@author: ADMIN
"""

def find_max(a, b, c):
    """Tìm số lớn nhất trong ba số nguyên."""
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    
    return maximum

def main():
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    c = int(input("Nhập số nguyên c: "))
    maximum = find_max(a, b, c)
    print(f"Số lớn nhất trong ba số là: {maximum}")

if __name__ == "__main__":
    main()
