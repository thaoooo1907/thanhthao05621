# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:23:01 2024

@author: ADMIN
"""

def time_to_seconds(hours, minutes, seconds):
    """Chuyển đổi giờ, phút, giây thành tổng số giây."""
    return hours * 3600 + minutes * 60 + seconds

def seconds_to_time(total_seconds):
    """Chuyển đổi tổng số giây thành giờ, phút, giây."""
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

def add_times(h1, m1, s1, h2, m2, s2):
    """Cộng hai thời điểm (giờ, phút, giây)."""
    total_seconds1 = time_to_seconds(h1, m1, s1)
    total_seconds2 = time_to_seconds(h2, m2, s2)
    total_seconds = total_seconds1 + total_seconds2
    return seconds_to_time(total_seconds)

def subtract_times(h1, m1, s1, h2, m2, s2):
    """Trừ hai thời điểm (giờ, phút, giây)."""
    total_seconds1 = time_to_seconds(h1, m1, s1)
    total_seconds2 = time_to_seconds(h2, m2, s2)
    total_seconds = total_seconds1 - total_seconds2
  
    total_seconds = max(total_seconds, 0)
    return seconds_to_time(total_seconds)

def main():
   
    h1 = int(input("Nhập giờ của thời điểm đầu tiên: "))
    m1 = int(input("Nhập phút của thời điểm đầu tiên: "))
    s1 = int(input("Nhập giây của thời điểm đầu tiên: "))
    
    
    h2 = int(input("Nhập giờ của thời điểm thứ hai: "))
    m2 = int(input("Nhập phút của thời điểm thứ hai: "))
    s2 = int(input("Nhập giây của thời điểm thứ hai: "))
    
    
    h_add, m_add, s_add = add_times(h1, m1, s1, h2, m2, s2)
    print(f"Tổng của hai thời điểm là: {h_add} giờ {m_add} phút {s_add} giây")
    
    
    h_sub, m_sub, s_sub = subtract_times(h1, m1, s1, h2, m2, s2)
    print(f"Hiệu của hai thời điểm là: {h_sub} giờ {m_sub} phút {s_sub} giây")

if __name__ == "__main__":
    main()
