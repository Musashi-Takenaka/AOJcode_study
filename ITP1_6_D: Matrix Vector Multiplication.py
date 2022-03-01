#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##### 入力
n, m = map(int, input().split())

##### 行列および列ベクトルの作成
### input().split()で空白区切りの文字列を取得 
### → intに変換 → list関数で囲み、リストとしてm個の数値を受け取る
### さらに【for _ in range(n)】でm個の数値の受け取りをn回行う
A = [list(map(int, input().split())) for _ in range(n)]

### 1つの整数の入力をm回繰り返す
b = [int(input()) for _ in range(m)]

##### 繰り返し処理で行列計算
for i in range(n):
    sum = 0
    for j in range(m):
        sum += A[i][j] * b[j]
    print(sum)
