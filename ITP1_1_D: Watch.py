! /usr/bin/env python
-*- coding: utf-8 -*-

"""
Q. 秒単位の時間 S が与えられるので、h:m:s の形式へ変換
"""

##### データ読み込み
S = int(input())

##### %dで整数値を代入
print("%d:%d:%d" % (S/3600, (S%3600)/60, S%60))
