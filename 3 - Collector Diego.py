with open('input.txt', 'r') as f:
    n = int(f.readline())
    diego = list(map(int, f.readline().split()))
    k = int(f.readline())
    kolls = list(map(int, f.readline().split()))

diego = list(set(diego))
ln = len(diego) - 1
diego.sort()

for kol in kolls:

    low = 0
    high = ln
    while low <= high:
        mid = (high + low) // 2
        try:
            if diego[mid] < kol < diego[mid + 1]:
                print(mid + 1)
                break
            elif mid == 0 and kol < diego[mid]:
                print(0)
                break
            elif kol == diego[mid]:
                print(mid)
                break
        except IndexError:
            if diego[mid] < kol:
                print(mid + 1)
                break

        if kol < diego[mid]:
            high = mid - 1
        elif kol > diego[mid]:
            low = mid + 1

