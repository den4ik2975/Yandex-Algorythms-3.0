from math import ceil
n = int(input())
k = int(input())
desk = int(input())
side = int(input())

pet = ((desk - 1) * 2) + side
var_pet = pet % k
if var_pet == 0:
    var_pet = k

van_1 = pet - k
van_2 = pet + k
if van_2 > n:
    if van_1 <= 0:
        print(-1)
    elif van_1 > 0:
        if van_1 % 2 == 1:
            print((van_1 // 2) + 1, 1)
        else:
            print(van_1 // 2, 2)
elif van_2 <= n and van_1 > 0:
    rast_1 = abs(desk - ceil(van_1 / 2))
    rast_2 = abs(desk - ceil(van_2 / 2))
    if rast_1 < rast_2:
        if van_1 % 2 == 1:
            print((van_1 // 2) + 1, 1)
        else:
            print(van_1 // 2, 2)
    else:
        if van_2 % 2 == 1:
            print((van_2 // 2) + 1, 1)
        else:
            print(van_2 // 2, 2)
elif van_2 <= n:
    if van_2 % 2 == 1:
        print((van_2 // 2) + 1, 1)
    else:
        print(van_2 // 2, 2)