
in1 = input()
in1 = int(in1)

out = 0
for i in range(1, in1+1) :
    out += i
    if(out>=in1) :
        print(i)
        break



