! /usr/bin/env python
-*- coding: utf-8 -*-

##### 入力
n = int(input())

#####　繰り返し処理
for i in range(1,n+1):
    ### 3で割り切れるか判定
    if i % 3 == 0:
        print(" {0}".format(i), end="")
    ### 10で割り算を繰り返して3を含む桁があるのか判定
    else:
        x = i
        while x != 0:
            if x % 10 == 3:
                print(" {0}".format(i), end="")
                break;
            x //= 10;
print("")
