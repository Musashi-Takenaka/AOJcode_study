#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##### リスト内包表記をネストして10部屋、3階建ての公舎4棟の組み合わせを作成
##### 10*3*4の0テンソル
houses = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]

##### 入力
n = int(input())

##### 入力値からの人数入力
for i in range(n):
    ### 4つの整数b(棟), f(階), r(番目), v(人)の読み込み
    b, f, r, v = map(int, input().split())
    ### 全て0が設定されたリスト(houses)10×3×4の組み合わせのb(棟), f(階), r(番目)にv(人)を設定
    houses[b - 1][f - 1][r - 1] += v

##### 出力
##### range(4)で0-3の繰り返し
for b in range(4):
    ### b(棟)の情報を表示
    for f in houses[b]:
        print('', *f)
    ### 区切り(####################)を表示
    if b != 3:
        print('#' * 20)
