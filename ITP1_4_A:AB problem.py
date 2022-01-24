! /usr/bin/env python
-*- coding: utf-8 -*-

"""
２つの整数 a と b を読み込んで、以下の値を計算する
a ÷ b ： d (整数)
a ÷ b の余り ： r (整数)
a ÷ b ： f (浮動小数点数；0.00001以下の誤差)
"""

a, b = map(int, input().split())
print('{0} {1} {2:.5f}'.format(a//b, a % b, a/b))
