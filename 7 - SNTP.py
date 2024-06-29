a = list(map(int, input().split(':')))
b = list(map(int, input().split(':')))
c = list(map(int, input().split(':')))

send = a[0] * 3600 + a[1] * 60 + a[2]
serv = b[0] * 3600 + b[1] * 60 + b[2]
recieve = c[0] * 3600 + c[1] * 60 + c[2]

if recieve < send:
    recieve += (24 * 60 * 60)

lamb = (recieve - send) / 2
if int(lamb) != lamb:
    lamb = int(lamb) + 1

serv += lamb
h = int(serv // 3600)
m = int((serv % 3600) // 60)
s = int(serv % 60)
if h >= 24:
    h -= 24
if h <= 9:
    h = f'0{int(h)}'
if m <= 9:
    m = f'0{int(m)}'
if s <= 9:
    s = f'0{int(s)}'
print(f'{h}:{m}:{s}')