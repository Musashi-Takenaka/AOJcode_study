! /usr/bin/env python
-*- coding: utf-8 -*-

"""
３つの整数 a、b、c を読み込み、a から b までの整数の中に、c の約数がいくつあるかを求めるプログラムを作成
1≤a,b,c≤10000
a≤b
"""

##### 分割して整数型へ変換
a, b, c = map(int, input().split())

##### 約数を繰り返し探索
num = 0

for i in range (a, b+1, 1):
    if c%i == 0:
        num += 1

print(num) 
