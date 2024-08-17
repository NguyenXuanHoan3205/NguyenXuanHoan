# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:00:30 2024

@author: Nguyen Xuan Hoan - 23694771
"""

a = float(input("Nhap canh cua a: "))
b = float(input("Nhap canh cua b: "))
c = float(input("Nhap canh cua c: "))
if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    print("a,b,c la ba canh cua mot tam giac.")
else:
    print("a,b,c khong phai la ba canh cua mot tam giac.")
    