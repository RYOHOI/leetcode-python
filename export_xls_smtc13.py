#! /usr/bin/env python   
# -*- coding: utf-8 -*-   
import xlwt, ast

wb = xlwt.Workbook()
ws = wb.add_sheet('First Sheet')

raw = open('students.txt').read()
students = ast.literal_eval(raw)

row, col = 0, 0
while row in range(3):
	key = str(row + 1)
	print students[key][col]
	ws.write(row, col, students[key][col].decode('utf-8'))
	for col in range(3):
		col += 1
		ws.write(row, col, students[key][col])
	col = 0
	row = row + 1
wb.save('sample.xls')