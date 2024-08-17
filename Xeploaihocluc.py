# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:27:24 2024

@author: Nguyen Xuan Hoan - 23694771
"""

gpa = float(input("Nhap diem trung binh (GPA): "))
if gpa < 3.5:
    print("Hoc luc kem")
elif 3.5 <= gpa < 5.0:
    print("Hoc luc Yeu")
elif 5.0 <= gpa < 7.0:
    print("Hoc luc trung binh")
elif 7.0 <= gpa < 8.0:
    print("Hoc luc kha")
elif 8.0 <= gpa < 9.0:
    print("Hoc luc gioi")
elif 9.0 <= gpa < 10:
    print("Hoc luc xuat sac")
else:
    print("Diem GPA khong hop le. Vui long nhap mot so trong khoang tu 0 toi 10.")
    
    
    
      
    

     
    