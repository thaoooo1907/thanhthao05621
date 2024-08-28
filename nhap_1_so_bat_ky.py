# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:32:23 2024

@author: ADMIN
"""

def number_to_word(number):
    """Chuyển đổi số nguyên từ 0 đến 9 thành chuỗi tương ứng."""
    words = {
        0: "Khong",
        1: "Mot",
        2: "Hai",
        3: "Ba",
        4: "Bon",
        5: "Nam",
        6: "Sau",
        7: "Bay",
        8: "Tam",
        9: "Chin"
    }
    return words.get(number, "Khong doc duoc")

def main():
    try:
        
        number = int(input("Nhập một số nguyên: "))
        
       
        result = number_to_word(number)
        
       
        print(result)
    
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")

if __name__ == "__main__":
    main()
