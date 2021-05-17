a = "abcde"

print(a[2])
print(len(a))

if len(a) % 2 == 1:
    slen = len(a)
    answer = a[int((slen-1)//2)]
else:
    slen = len(a)
    answer = a[int((slen-1)//2):int(slen-1)]

print(answer)