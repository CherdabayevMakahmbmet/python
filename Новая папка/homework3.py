v = int(input('SEC: '))
h = v // 3600
m = (v % 3600) // 60
s = (v % 3600) % 60
b = h / 24
if b == int(b):
    h = 0
elif h > 24:
    h = h - 24 * (h // 24)
if m < 10:
    m = "0" + str(m)
if s < 10:
    s = "0" + str(s)
print('Time: ', str(h), ":", str(m), ":", str(s))


129700