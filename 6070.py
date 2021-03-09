
month = input()
month = int(month)
if(month==1 or month==2 or month==12) : print("winter")
elif(3<=month and month<6) : print("spring")
elif(6<=month and month<9) : print("summer")
elif(9<=month and month<12) : print("fall")
else : print("input a number between 1 to 12")
