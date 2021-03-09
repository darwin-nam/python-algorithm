
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
x = a if(a<b) else b 
y = a if(a<c) else c
z = x if(x<y) else y
print(z)

