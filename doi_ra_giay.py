# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:11:32 2024

@author: ADMIN
"""

def convert_to_seconds(hours, minutes, seconds):
    """Chuyển đổi giờ, phút, giây thành tổng số giây."""
    return hours * 3600 + minutes * 60 + seconds

def main():
    try:
        time_input = input("Nhập thời gian theo định dạng 'giờ phút giây' (ví dụ: 1 8 30): ")
        h, m, s = map(int, time_input.split())
        total_seconds = convert_to_seconds(h, m, s)
        print(f"Tổng số giây là: {total_seconds}")
    
        
    
    except ValueError:
        print("Định dạng đầu vào không hợp lệ. Vui lòng nhập theo định dạng 'giờ phút giây'.")

if __name__ == "__main__":
    main()
