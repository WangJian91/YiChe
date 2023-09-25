# -*- coding: utf-8 -*-
import random

employee_list = [i for i in range(1, 301)]
random.shuffle(employee_list)
num = 0
for i in range(3):
    num += 1
    if num == 1:
        print(f'恭喜员工{employee_list[-1]}获得三等奖：三斤苹果')
    elif num == 2:
        print(f'恭喜员工{employee_list[-1]}获得二等奖：iPhone14手机')
    else:
        print(f'恭喜员工{employee_list[-1]}获得一等奖：泰国5日游+手术费报销')
    employee_list.pop()
    random.shuffle(employee_list)
