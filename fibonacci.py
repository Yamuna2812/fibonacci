num=int(input("Enter the the fibonacci sequence lenght to be generated:"))
firstnum = 0
secondnum = 1
print("The fibonacci series with",num,"term is:")
print(firstnum,secondnum,end=" ")
for i in range(2,num):
    curnum=firstnum+secondnum
    print(curnum,end=" ")
    firstnum = secondnum
    secondnum = curnum



