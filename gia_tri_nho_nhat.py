# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:24:33 2024

@author: ADMIN
"""

def find_smallest(a, b, c, d):
    """Tìm số nhỏ nhất trong bốn số nguyên."""
    smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    if d < smallest:
        smallest = d
    
    return smallest

def main():
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    c = int(input("Nhập số nguyên c: "))
    d = int(input("Nhập số nguyên d: "))
    smallest = find_smallest(a, b, c, d)
    print(f"Số nhỏ nhất trong bốn số là: {smallest}")

if __name__ == "__main__":
    main()
