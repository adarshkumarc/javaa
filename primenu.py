lower=10
high=100
print("prime number between ",lower,"and ",high,"are")
for num in range(lower,high+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
            else:
                print(num)