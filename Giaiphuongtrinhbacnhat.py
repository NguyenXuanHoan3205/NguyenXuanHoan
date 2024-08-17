# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:04:49 2024

@author: Nguyen Xuan Hoan - 23694771
"""

a = float(input("Nhap gia tri cua a: "))
b = float(input("Nhap gia tri cua b: "))
if a == 0:
    if b == 0:
        print("Phuong trinh co vo so nghiem.")
    else:
        print("Phuong trinh vo nghiem.")
else:
    x = -b / a
    print("Nghiem cua phuong trinh la:", x)
    
    
    